# Status and Roadmap

[← Back to Broiler Platform](https://github.com/Broiler-Platform)

Broiler is under active development and is **not yet intended for production use**. This summary was reconciled with the aggregate checkout on **21 October 2026**; implementation, test evidence and release acceptance are separate claims.

## Platform snapshot

| Area | Current repository evidence |
|---|---|
| Repository composition | 26 component submodules; 70 declared cross-component product dependency edges |
| Applications | Browser, Writer, Code, Plate and Mail; Fond under development |
| Application targets | Windows, Linux, Android; Writer also has a WebAssembly head |
| Mail targets | Windows and Android; Linux remains a placeholder |
| Self-hosting | BOSS serves the WebAssembly Writer through ASP.NET Core |
| Document codecs | RTF, HTML, Markdown, DOCX, ODT, CSV; PDF logical-text import and PDF 1.7 writing remain preview capabilities |
| NativeAOT | Writer Windows/Linux and Plate Windows publish paths; Mail Windows x64/ARM64 validation packaging |
| Broiler.VM | Core and JavaScript/WebAssembly profiles implemented in part; VM-0 through VM-7 in progress and unaccepted |

## Standards and visual evidence

Test262, WPT, WPT reftests, public-site render comparisons and privacy-page probes are separate validation surfaces. This documentation update did not run them. Earlier figures (>99.99% Test262; 93%/85% Chromium agreement; 84% pixel-identical reftests) lack a revision-linked report here and are not presented as current measurements.

The aggregate [roadmap](https://github.com/Broiler-Platform/Broiler/blob/main/docs/ROADMAP.md) still calls for a reproducible, pinned Chromium/WPT baseline and fresh Acid and real-world rendering evidence. A Chromium comparison is not a WPT pass rate; matching a reference image does not establish JavaScript conformance or security. Existing [screenshots](screenshots.md) are illustrative development captures.

## Implemented and in progress

- Shared DOM, CSS, layout, HTML rendering, JavaScript, graphics, input, media, document and UI components exist, with component-owned validation suites.
- Code includes workspace and C# language-service projects and content-based per-file human-review tooling.
- Mail has single-account reading, SMTP composition and HTML preview work. Provider acceptance and renderer process isolation remain release gates; generated packages are unsigned validation builds.
- Documents provides explicit codec composition. PDF is a subset implementation with optional font and image providers; package generation does not certify PDF conformance or enable every application feature.
- Printing work includes pagination and PDF spool primitives; the aggregate printing roadmap retains platform and application delivery gates.
- Fond milestone 1 is in progress, including an in-memory kernel and bounded FinTS parsing against synthetic fixtures. Authenticated protocol security remains pending.
- VM includes JavaScript and WebAssembly profiles, bytecode execution and native artifact backends. x86-64 execution exists; ARM64 is emitting-only. No accepted VM milestone or advertised support follows from those implementations.

## Remaining priorities

Current component and aggregate roadmaps track web compatibility and performance, reproducible standards evidence, release and installation paths, printing, collaboration, Android and hardware validation, accessibility, and security review. NuGet package metadata and publish workflows exist; release readiness must be checked against the exact component revision and its review record.

Use the [aggregate documentation index](https://github.com/Broiler-Platform/Broiler/blob/main/docs/README.md) to find component-owned plans. For VM acceptance, use its [authoritative status ledger](https://github.com/Broiler-Platform/Broiler.VM/blob/main/docs/roadmap.status.md), rather than inferring completion from a project or API being present.

## Source records

This summary follows component-owned records: [Mail overview](https://github.com/Broiler-Platform/Broiler.Mail/blob/main/README.md), [Documents formats and PDF gates](https://github.com/Broiler-Platform/Broiler.Documents/blob/main/README.md), [Fond milestone status](https://github.com/Broiler-Platform/Broiler.Fond/blob/main/README.md), and [VM status](https://github.com/Broiler-Platform/Broiler.VM/blob/main/docs/roadmap.status.md). The [graph snapshot](component-map.json) pins the checked component commits; linked main-branch pages can move after this snapshot.
