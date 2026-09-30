# Broiler Platform

> **Browser and Office Infrastructure in Intermediate Language with Enhanced Reliability**

[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/Broiler-Platform/.github/blob/main/LICENSE)
[![Releases](https://img.shields.io/badge/releases-preview-brightgreen.svg)](https://github.com/Broiler-Platform/Broiler/releases)
[![Platforms](https://img.shields.io/badge/platforms-Windows%20%7C%20Linux%20%7C%20Android%20%7C%20WebAssembly-lightgrey.svg)](https://github.com/Broiler-Platform/.github/blob/main/profile/docs/architecture.md)

Broiler is an open-source software platform exploring a deliberately ambitious question:

> **Can modern browser and office applications be built entirely in managed .NET?**

No Chromium. No embedded WebView. No native browser engine. Just managed .NET, modular architecture, open standards, automated verification, AI-assisted engineering, and human review.

Broiler is **not** a wrapper around an existing browser or office stack. It is a reusable platform for building browsers, office applications, document software, and future web-enabled tools on top of a shared managed runtime — built around a simple idea:

> Important application infrastructure should remain understandable, inspectable, portable, and replaceable.

> [!NOTE]
> Broiler is under active development and is **not yet intended for production use**.

---

## Platform Snapshot

| Component | Status |
|-----------|--------|
| ECMAScript (Test262) | **>99.99% passing** |
| WPT — ≥90% Chromium agreement | **93%** |
| WPT — ≥97% Chromium agreement | **85%** |
| WPT Reftests — pixel-identical | **84%** |
| Supported Platforms | Windows, Linux, Android, WebAssembly |
| Applications | Browser, Writer, Code, Plate, Mail |
| Reference Deployment | BOSS |
| Document Formats | RTF, HTML, Markdown, DOCX, ODT, PDF *(preview)* |
| Native Compilation | Writer *(win-x64, linux-x64)* and Plate *(win-x64)* publish with **NativeAOT** |
| Repository Layout | 25 independently versioned repositories — 5 applications on 20 platform components ([Component Map](https://github.com/Broiler-Platform/.github/blob/main/profile/docs/component-map.md)) |

---

## Architecture at a Glance

Every component is its own repository, consumed by the layer above it as a versioned
NuGet package. Nothing in a lower layer knows about anything above it — the dependency
graph is acyclic, and it is derived from the build files rather than drawn by hand.

```text
                            Broiler Platform

  APPLICATIONS   Broiler.Browser · Broiler.Writer · Broiler.Code
                 Broiler.Plate · Broiler.Mail
                              │
  PRESENTATION   Broiler.HtmlBridge · Broiler.HTML · Broiler.UI
                              │
  SEAM, LAYOUT   Broiler.JSeal · Broiler.Layout · Broiler.Documents
  & DOCUMENTS                 │
  ENGINES        Broiler.JS · Broiler.Graphics · Broiler.Input
  & DEVICES                   │
  PRIMITIVES     Broiler.CSS · Broiler.RegEx · Broiler.Media
  & CODECS                    │
  FOUNDATION     Broiler.DOM · Broiler.Unicode · Broiler.VM
                 Broiler.Net · Broiler.Native
```

The full wiring — who depends on whom, in both directions — is in the
**[Component Map](https://github.com/Broiler-Platform/.github/blob/main/profile/docs/component-map.md)**.

[![Broiler component map](https://raw.githubusercontent.com/Broiler-Platform/.github/main/profile/component-map.png)](https://github.com/Broiler-Platform/.github/blob/main/profile/docs/component-map.md)

### Applications

| Application | What it is | Heads |
|-------------|------------|-------|
| **Broiler Browser** | Reference browser — the full web stack end to end | Windows, Linux, Android |
| **Broiler Writer** | Word processor and reference office application | Windows, Linux, Android, WebAssembly |
| **Broiler Code** | Code editor with C# language services and a human-review workspace | Windows, Linux |
| **Broiler Plate** | Read-only viewer — the smallest honest demonstration of what the platform can already read | Windows |
| **Broiler Mail** | Mail client; v1 is a single-account reader, v2 adds SMTP sending | Windows, Linux |
| **BOSS** | Broiler Office Standalone Server — hosts the WebAssembly Writer via ASP.NET Core | self-hosted |

---

## Enhanced Reliability

The **"Enhanced Reliability"** part of the name reflects the project's engineering philosophy.

```text
Managed .NET
+ Modular Architecture
+ Open Standards
+ AI-Assisted Engineering
+ Human Review
+ Automated Verification
--------------------------------------------------
= Enhanced Reliability
```

AI can generate code rapidly. Reliable browser and office infrastructure requires considerably more. Broiler therefore combines AI-assisted development with modular design, standards compliance, automated verification, and human review.

Each part of that formula is described in [Engineering Principles](https://github.com/Broiler-Platform/.github/blob/main/profile/docs/principles.md).

---

## Documentation

| Document | Contents |
|----------|----------|
| [Status and Roadmap](https://github.com/Broiler-Platform/.github/blob/main/profile/docs/status.md) | What works today, what is in progress, what comes next |
| [Architecture and Deployment](https://github.com/Broiler-Platform/.github/blob/main/profile/docs/architecture.md) | Platform layers, desktop/mobile/web, self-hosting, open infrastructure |
| [Component Map](https://github.com/Broiler-Platform/.github/blob/main/profile/docs/component-map.md) | Every component, what it owns, and what it depends on — in both directions |
| [Engineering Principles](https://github.com/Broiler-Platform/.github/blob/main/profile/docs/principles.md) | Managed .NET, standards first, security, modularity, AI + human review |
| [Why Broiler](https://github.com/Broiler-Platform/.github/blob/main/profile/docs/why-broiler.md) | Why the platform exists, why .NET, why another browser and office |
| [Project Story](https://github.com/Broiler-Platform/.github/blob/main/profile/docs/project-story.md) | How Broiler started, and acknowledgements |
| [Native Compilation](https://github.com/Broiler-Platform/.github/blob/main/profile/docs/native-compilation.md) | NativeAOT: self-contained native binaries, and what that constrains |
| [Current Preview](https://github.com/Broiler-Platform/.github/blob/main/profile/docs/screenshots.md) | Screenshots of the browser, the writer, and standards tests |

---

## Getting Started

- [Download the latest Preview Release](https://github.com/Broiler-Platform/Broiler/releases)
- Explore the [source code](https://github.com/Broiler-Platform/Broiler)
- Try [Browser](https://github.com/Broiler-Platform/Broiler.Browser), [Writer](https://github.com/Broiler-Platform/Broiler.Writer), [Code](https://github.com/Broiler-Platform/Broiler.Code), [Plate](https://github.com/Broiler-Platform/Broiler.Plate) or [Mail](https://github.com/Broiler-Platform/Broiler.Mail)
- Run the Writer through BOSS
- Build on the platform directly — components publish as NuGet preview packages
- [Report bugs and compatibility problems](https://github.com/Broiler-Platform/Broiler/issues)

Feedback and contributions are always appreciated.

---

## Contributing

Contributions of all kinds are welcome — code, documentation, testing, ideas, interoperability reports, or security analysis.

Please read `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md` and `SECURITY.md` before opening a pull request.

---

## License

Broiler is licensed under the **Apache License 2.0**.
