# Contributing to Broiler

Thanks for your interest in Broiler. Contributions of all kinds are welcome — code, documentation, testing, compatibility reports, ideas, and security analysis.

This guide applies to every repository in the [Broiler-Platform](https://github.com/Broiler-Platform) organization.

---

## Ways to contribute

You do not need to write engine code to be useful. Some of the most valuable contributions are:

| Contribution | Where it goes |
|---|---|
| **Compatibility reports** — a real site that renders wrongly | [Issues](https://github.com/Broiler-Platform/Broiler/issues), with the URL and a screenshot |
| **Reduced test cases** — a minimal HTML/CSS/JS file that reproduces a bug | Issues, inline in the report |
| **Bug fixes and features** | Pull request to the relevant repository (see below) |
| **Documentation** | Pull request to the repository whose behavior it describes |
| **Security issues** | **Not** an issue — see [SECURITY.md](https://github.com/Broiler-Platform/.github/blob/main/SECURITY.md) |

A small, well-reduced test case is often worth more than a long bug description.

---

## Where to open your pull request

This is the part that trips up new contributors. [`Broiler-Platform/Broiler`](https://github.com/Broiler-Platform/Broiler) is an umbrella repository: the engine components are **git submodules** pointing at their own repositories.

That means a fix to the CSS engine belongs in `Broiler-Platform/Broiler.CSS`, **not** in the umbrella repo.

| If you are changing… | Open the PR against |
|---|---|
| JavaScript engine | [`Broiler.JS`](https://github.com/Broiler-Platform/Broiler.JS) |
| CSS parsing and cascade | [`Broiler.CSS`](https://github.com/Broiler-Platform/Broiler.CSS) |
| HTML parsing and rendering | [`Broiler.HTML`](https://github.com/Broiler-Platform/Broiler.HTML) |
| DOM | [`Broiler.DOM`](https://github.com/Broiler-Platform/Broiler.DOM) |
| Graphics and text shaping | [`Broiler.Graphics`](https://github.com/Broiler-Platform/Broiler.Graphics) |
| UI framework | [`Broiler.UI`](https://github.com/Broiler-Platform/Broiler.UI) |
| Input abstraction | [`Broiler.Input`](https://github.com/Broiler-Platform/Broiler.Input) |
| Media | [`Broiler.Media`](https://github.com/Broiler-Platform/Broiler.Media) |
| Document model and formats | [`Broiler.Documents`](https://github.com/Broiler-Platform/Broiler.Documents) |
| Browser or Writer application shell | [`Broiler.Browser`](https://github.com/Broiler-Platform/Broiler.Browser) / [`Broiler.Writer`](https://github.com/Broiler-Platform/Broiler.Writer) |
| Layout, CLI, WPT runner, BOSS, build and tooling | [`Broiler`](https://github.com/Broiler-Platform/Broiler) |

If a change spans several components, open a PR per repository and link them to each other. If you are unsure where something belongs, open an issue on the umbrella repository first and ask.

---

## Building and testing

Broiler targets **.NET 10**. Clone with submodules — the build will not work without them:

```bash
git clone --recurse-submodules https://github.com/Broiler-Platform/Broiler.git
```

If you already cloned without `--recurse-submodules`:

```bash
git submodule update --init --recursive
```

Full build, test, and run instructions live in the [Broiler README](https://github.com/Broiler-Platform/Broiler#build-and-test) — they are maintained there so they stay next to the code.

Two things worth knowing before your first build:

- Broiler uses **platform-specific configurations** rather than plain `Debug` and `Release`: `Debug-Windows`, `Release-Windows`, `Debug-Linux`, `Release-Linux`. Pass the one matching your target.
- Solutions are `.slnx` files, split by target and purpose (`Broiler.Windows.Code.slnx`, `Broiler.Tests.slnx`, `Broiler.Wpt.slnx`, `Broiler.Office.Server.slnx`, and others). Build the one covering your change rather than everything.

Run the test suite before opening a PR:

```bash
dotnet test Broiler.Tests.slnx
```

Changes to engine behavior should also be checked against the standards suites — the Test262, WPT, and reftest runners under `scripts/` — so that a fix in one area does not regress another.

---

## Standards and compatibility

Broiler measures compatibility rather than guessing at it, and that shapes what a good change looks like:

- **Cite the spec.** When implementing or fixing web-platform behavior, reference the relevant specification section in your PR description.
- **Do not regress the suites.** A change that fixes one site but lowers Test262 or WPT pass rates will not be merged as-is.
- **Match the standard, not another browser.** Where implementations disagree, the specification wins. Where the specification is genuinely ambiguous, say so in the PR and explain the choice.
- **Add a test.** New behavior needs coverage; a bug fix should come with the reduced case that reproduced it.

---

## Code guidelines

- **Managed .NET first.** Core engines and subsystems are implemented in managed .NET. Native interop is confined to the platform integration layer, where the operating system genuinely requires it (for example Direct2D, DirectWrite, and DXGI in the Windows graphics backend). Do not introduce native dependencies elsewhere, and do not take on a browser engine, embedded WebView, or similar as a dependency.
- **Stay modular.** Respect existing component boundaries. A component should not reach into the internals of another component to get something done.
- **Match the surrounding code.** Follow the conventions of the file you are editing rather than importing a different style.
- **Keep changes focused.** One logical change per pull request. Unrelated cleanup belongs in its own PR.
- **Note the nullable state.** Some projects enable `<Nullable>` and some do not, and a set of nullable warnings is suppressed repository-wide during an incremental migration. Do not suppress more warnings to make a change compile.

---

## AI-assisted contributions

Broiler is built with AI assistance, and AI-assisted pull requests are welcome. The project's position is that AI is an engineering tool, not the owner of the codebase — so the bar is the same either way:

- **You are responsible for what you submit.** Be able to explain what your change does and why it is correct.
- **Understand it before you send it.** Do not open a PR containing code you have not read and cannot discuss in review.
- **Test it.** Generated code that has not been run is not a contribution.
- **Every contribution is reviewed by a human before it is merged**, regardless of how it was produced.

Several components carry `HUMAN_REVIEW.md` records documenting their review status, reviewer attestations, and outstanding conditions. Changes to reviewed code may require that component to be re-reviewed, so expect a security-sensitive change to take longer to land.

---

## Pull request checklist

Before you open a PR:

- [ ] It targets the right repository (see the table above)
- [ ] It builds with the appropriate platform configuration
- [ ] `dotnet test Broiler.Tests.slnx` passes
- [ ] Standards suites are not regressed, where the change could affect them
- [ ] Tests cover the new behavior or the fixed bug
- [ ] The description explains **why**, not only what — with a spec reference where relevant
- [ ] Any new third-party dependency is recorded in `THIRD_PARTY_NOTICES.md` with a compatible license
- [ ] It contains no security-sensitive disclosure that should have gone through [SECURITY.md](https://github.com/Broiler-Platform/.github/blob/main/SECURITY.md) instead

Expect review comments. Browser and document infrastructure is subtle, and questions on a PR are about the code, not about you.

---

## Licensing

Broiler is licensed under the **Apache License 2.0**. By contributing, you agree that your contributions are licensed under the same terms.

Only contribute code you have the right to contribute. If you adapt code from another project, say so in the PR, confirm the license is compatible with Apache 2.0, and add the required attribution to `THIRD_PARTY_NOTICES.md` and the `LICENSES` directory.

---

## Code of Conduct

All participation in Broiler-Platform is governed by the [Code of Conduct](https://github.com/Broiler-Platform/.github/blob/main/CODE_OF_CONDUCT.md). Please read it before taking part.
