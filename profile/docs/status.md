# Status and Roadmap

[← Back to Broiler Platform](https://github.com/Broiler-Platform)

Broiler is under active development and is **not yet intended for production use**.

---

## Platform Snapshot

| Component | Status |
|-----------|--------|
| ECMAScript (Test262) | **>99.99% passing** |
| WPT — ≥90% Chromium agreement | **93%** |
| WPT — ≥97% Chromium agreement | **85%** |
| WPT Reftests — pixel-identical | **84%** |
| Supported Platforms | Windows, Linux, Android |
| Reference Applications | Browser, Writer |
| Reference Deployment | BOSS |
| Document Formats | RTF, HTML, Markdown, DOCX |

---

## Implemented

### Core Platform

- ECMAScript / JavaScript engine
- HTML runtime
- CSS engine
- Layout engine
- Document model
- Rich text engine
- Platform-independent UI framework
- Platform-independent input abstraction
- Graphics infrastructure
- Browser runtime
- Office runtime

### Applications

- **Broiler Browser**
- **Broiler Writer**
- **Broiler Office Standalone Server (BOSS)**

### Platforms

- Windows
- Linux
- Android
- WebAssembly-based Writer deployment through BOSS

### Document Support

- RTF
- HTML
- Markdown
- DOCX

### Automated Verification

- Test262
- Web Platform Tests (WPT)
- WPT Reftests
- Continuous standards and rendering validation

---

## In Progress

- HTML and CSS compatibility improvements
- Layout engine refinements
- Cross-platform graphics improvements
- Browser shell improvements
- WebAssembly improvements
- Performance optimization
- Broader device and platform validation

---

## Roadmap

Current priorities include:

- Higher WPT compatibility
- Improved real-world website compatibility
- HTML and CSS improvements
- Browser shell improvements
- WebAssembly improvements
- Cross-platform graphics
- Office collaboration infrastructure
- PDF support
- Printing
- Security hardening
- Performance optimization
- Broader Android and device validation
- Reusable NuGet packages for platform components

The project is currently moving from combined development snapshots toward separately versioned Preview Releases and reusable NuGet packages.
