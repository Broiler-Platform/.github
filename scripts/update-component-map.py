"""Rebuild the documentation graph from component-owned tracked project files.

Usage: python scripts/update-component-map.py D:/Broiler
Requires Python 3 and Pillow; bitmap rendering uses Windows Segoe UI.
No restore or build is performed. Conditions are retained as evidence, not evaluated.
"""
import argparse
import datetime
import json
import re
import subprocess
import xml.etree.ElementTree as ET
from pathlib import Path

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('source', type=Path)
args = parser.parse_args()
root = args.source.resolve()
out = Path(__file__).resolve().parents[1] / 'profile'

def git(path, *args):
    return subprocess.check_output(['git', '-C', str(path), *args], text=True, encoding='utf-8').strip()

components = sorted(re.findall(r'path = (Broiler\.[^\s]+)', (root / '.gitmodules').read_text()))
projects = []
for component in components:
    for name in git(root / component, 'ls-files', '*.csproj').splitlines():
        # Exclude validation, tooling and samples; nested submodule files are not tracked here.
        if re.search(r'(^|/)(tests?|samples?|demos?|benchmarks?|eng|tools|docs)(/|\.)|Tests?\.|\.Tests?\b|Benchmarks?|\.Demo\b', name, re.I):
            continue
        path = root / component / name
        tree = ET.parse(path)
        if tree.findtext('.//IsTestProject', '').lower() == 'true':
            continue
        projects.append((component, name, tree))

packages = {}
for component, name, tree in projects:
    for package in (Path(name).stem, tree.findtext('.//PackageId'), tree.findtext('.//AssemblyName')):
        if package and '$(' not in package:
            packages[package.lower()] = component

def owner(package):
    if package.lower() in packages:
        return packages[package.lower()]
    for component in sorted(components, key=len, reverse=True):
        prefix = 'Broiler.Regex' if component == 'Broiler.RegEx' else component
        if package.lower() == prefix.lower() or package.lower().startswith(prefix.lower() + '.'):
            return component

edges = {c: set() for c in components}
evidence = []
for component, name, tree in projects:
    for group in tree.iter():
        for ref in group:
            if ref.tag not in ('PackageReference', 'ProjectReference'):
                continue
            include = ref.get('Include', '')
            target = owner(include if ref.tag == 'PackageReference' else Path(include.replace('\\', '/')).stem)
            if target and target != component:
                edges[component].add(target)
                evidence.append(dict(source=component, target=target, project=name, kind=ref.tag,
                                     reference=include, condition=' AND '.join(filter(None, [group.get('Condition'), ref.get('Condition')]))))

levels = {}
def level(c, trail=()):
    if c in trail:
        raise ValueError('Component cycle: ' + ' -> '.join((*trail, c)))
    if c not in levels:
        levels[c] = max((level(d, (*trail, c)) + 1 for d in edges[c]), default=0)
    return levels[c]
for c in components:
    level(c)
incoming = {c: sorted(s for s in components if c in edges[s]) for c in components}
ordered = sorted(components, key=lambda c: (-levels[c], c))
date = datetime.date.today().isoformat()
snapshot = dict(date=date, aggregate_commit=git(root, 'rev-parse', 'HEAD'),
                scope='Component-owned tracked product csproj files; all declared conditions included; no MSBuild evaluation; excludes tests, samples, demos, benchmarks, eng, tools and docs.',
                components=[dict(name=c, commit=git(root / c, 'rev-parse', 'HEAD'),
                                 tracked_changes=git(root / c, 'diff', '--name-only', 'HEAD'),
                                 projects=sum(p[0] == c for p in projects), level=levels[c], dependencies=sorted(edges[c])) for c in components],
                evidence=sorted(evidence, key=lambda e: (e['source'], e['project'], e['reference'])))
(out / 'docs/component-map.json').write_text(json.dumps(snapshot, indent=2) + '\n', encoding='utf-8')
ids = {c: 'C' + str(i) for i, c in enumerate(components)}
mermaid = ['graph TD'] + [f'    {ids[c]}["{c}"]' for c in ordered]
mermaid += [f'    {ids[c]} --> {ids[d]}' for c in ordered for d in sorted(edges[c])]
text = f'''# Component Map

[← Back to Broiler Platform](https://github.com/Broiler-Platform)

Updated from the aggregate checkout on **{date}**. The aggregate pins {len(components)} component repositories as Git submodules and also owns integration tools, tests and BOSS. It is not itself a node here.

## Reading the graph

Arrows point from consumer to dependency. This is the union of declared references in component-owned product `.csproj` files, including conditional references and optional providers. It is not the dependency closure of every application build. Tests, samples, demos, benchmarks, documentation and tooling directories are excluded; nested submodule copies are not scanned. Package IDs are mapped to their owning component. References imported from props/targets and resolved NuGet transitive dependencies are outside this scan.

The [machine-readable snapshot](component-map.json) records source commits, tracked changes, project counts and reference evidence. Regenerate from the documentation repository with `python scripts/update-component-map.py D:/Broiler`. Working-tree project contents are used; this records declarations, not a successful build, package availability or release approval.

## Diagram

![Broiler component map](../component-map.png)

```mermaid
{chr(10).join(mermaid)}
```

## Dependencies in both directions

Levels are computed as the longest dependency path to a leaf. An isolated node means no cross-component reference was found in this scan; it does not mean no implementation exists.

| Level | Component | Depends on | Used by |
|---:|---|---|---|
'''
for c in ordered:
    fmt = lambda values: ', '.join('`' + v + '`' for v in values) or '—'
    text += f'| {levels[c]} | **{c}** | {fmt(sorted(edges[c]))} | {fmt(incoming[c])} |\n'
text += '\n## Dependency counts\n\nCounts are distinct component edges, not package or assembly counts.\n\n| Component | Consumers (fan-in) | Dependencies (fan-out) |\n|---|---:|---:|\n'
for c in sorted(components, key=lambda c: (-len(incoming[c]), c)):
    text += f'| {c} | {len(incoming[c])} | {len(edges[c])} |\n'
text += '''
## Important boundaries

- JSEAL contracts are engine-neutral; `Broiler.JSeal.BroilerJs` and `Broiler.JSeal.Vm` provide engine-specific implementations. A component-level arrow from JSEAL to an engine describes a provider, not the contracts assembly.
- The Browser's VM configurations select an optional VM scripting provider. HtmlBridge's DOM binding still reaches Broiler.JS; selecting the VM does not remove that dependency.
- Broiler.VM contains core, JavaScript and WebAssembly profile projects and native artifact execution work. Its VM-0 through VM-7 milestones remain in progress and unaccepted; implementation does not establish supported deployment or human approval.
- Broiler.Fond has an in-progress finance kernel and synthetic protocol fixtures. Its application and authenticated banking capabilities remain under development.

See [Architecture](architecture.md), [Status](status.md), and [Native Compilation](native-compilation.md).
'''
(out / 'docs/component-map.md').write_text(text, encoding='utf-8')

# A code-generated overview keeps the bitmap synchronized with the same adjacency data.
from PIL import Image, ImageDraw, ImageFont
font_path = Path('C:/Windows/Fonts/segoeui.ttf')
font = ImageFont.truetype(str(font_path), 19)
small = ImageFont.truetype(str(font_path), 16)
title = ImageFont.truetype(str(font_path), 30)
# Separate consumer panels prevent long edges from crossing unrelated nodes.
# Each arrow below is emitted from exactly one recorded adjacency entry.
width = 1800
columns = 3
margin, gap, card_width = 35, 25, 560
rows = [ordered[i:i + columns] for i in range(0, len(ordered), columns)]
row_heights = [88 + 29 * max(max(len(edges[c]), 1) for c in row) for row in rows]
height = 125 + sum(row_heights) + gap * len(rows)
im = Image.new('RGB', (width, height), '#f8fafc')
draw = ImageDraw.Draw(im)
draw.text((35, 20), 'Broiler: direct dependencies by component', fill='#172b4d', font=title)
draw.text((35, 67), f'{date} · Each panel lists only its named consumer’s direct dependencies · All declared configurations', fill='#475569', font=small)
y = 115
for row, row_height in zip(rows, row_heights):
    for i, c in enumerate(row):
        x = margin + i * (card_width + gap)
        draw.rounded_rectangle((x, y, x + card_width, y + row_height), radius=10, fill='white', outline='#b7c5d5', width=2)
        draw.rounded_rectangle((x, y, x + card_width, y + 45), radius=10, fill='#e2ecfa')
        draw.text((x + 18, y + 10), c, fill='#172b4d', font=font)
        if not edges[c]:
            draw.text((x + 18, y + 61), 'No cross-component dependency found', fill='#64748b', font=small)
        for j, d in enumerate(sorted(edges[c])):
            dy = y + 68 + j * 29
            draw.line((x + 20, dy, x + 45, dy), fill='#496582', width=2)
            draw.polygon([(x + 45, dy), (x + 38, dy - 4), (x + 38, dy + 4)], fill='#496582')
            draw.text((x + 57, dy), d, anchor='lm', fill='#172b4d', font=font)
    y += row_height + gap
im.save(out / 'component-map.png')
print(f'{len(components)} components, {len(projects)} product projects, {sum(map(len, edges.values()))} component edges; graph is acyclic.')

