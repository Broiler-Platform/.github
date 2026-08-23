# Broiler Platform

> **Browser and Office Infrastructure in Intermediate Language with Enhanced Reliability**

[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)

**Latest Releases:** https://github.com/Broiler-Platform/Broiler/releases

---

# Welcome

Welcome to the **Broiler Platform**.

Broiler is an open-source software platform exploring a deliberately ambitious question:

> **Can modern browser and office applications be built entirely in managed .NET?**

No Chromium.

No embedded WebView.

No native browser engine.

Just managed .NET, modular architecture, open standards, automated verification, AI-assisted engineering, and human review.

Broiler is **not** a wrapper around an existing browser or office stack.

It is a reusable platform for building browsers, office applications, document software, and future web-enabled tools on top of a shared managed runtime.

The project is built around a simple idea:

> Important application infrastructure should remain understandable, inspectable, portable, and replaceable.

---

# Platform Snapshot

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

# Platform Architecture

```text
                            Broiler Platform

        ┌──────────────────────────────────────────────────────┐
        │                                                      │
        │ ECMAScript • DOM • CSS • Layout • Graphics           │
        │ UI • Input • Documents • Runtime                     │
        │                                                      │
        └─────────────────────┬────────────────────────────────┘
                              │
          ┌───────────────────┼────────────────────┐
          │                   │                    │
   Broiler Browser      Broiler Writer        WebAssembly
   Windows/Linux/       Windows/Linux/             │
      Android              Android                 │
                                                   │
                                                  BOSS
```

The browser and writer are the first reference applications built on top of the shared Broiler Platform.

BOSS demonstrates how the same document and UI infrastructure can also be deployed through WebAssembly and self-hosted using ASP.NET Core.

---

# Current Preview

These screenshots show the current state of Broiler during active development.

<table>
  <tr>
    <td width="50%">
      <img src="./google.png" alt="Google" />
    </td>
    <td width="50%">
      <img src="./7zorg.png" alt="7-Zip" />
    </td>
  </tr>
  <tr>
    <td align="center"><sub>google.de</sub></td>
    <td align="center"><sub>7-zip.org</sub></td>
  </tr>
  <tr>
    <td width="50%">
      <img src="./wpt.png" alt="Web Platform Tests" />
    </td>
    <td width="50%">
      <img src="./mozilla.png" alt="Mozilla" />
    </td>
  </tr>
  <tr>
    <td align="center"><sub>wpt.live</sub></td>
    <td align="center"><sub>ftp.mozilla.org</sub></td>
  </tr>
  <tr>
    <td width="50%">
      <img src="./writer.png" alt="Broiler Writer" />
    </td>
    <td width="50%">
      <img src="./acid1.png" alt="Acid1 Test" />
    </td>
  </tr>
  <tr>
    <td align="center"><sub>Broiler Writer</sub></td>
    <td align="center"><sub>Acid1</sub></td>
  </tr>
</table>

---

# Current Status

Broiler is under active development and is **not yet intended for production use**.

## Core Platform

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

## Applications

- **Broiler Browser**
- **Broiler Writer**
- **Broiler Office Standalone Server (BOSS)**

## Platforms

- Windows
- Linux
- Android
- WebAssembly-based Writer deployment through BOSS

## Document Support

- RTF
- HTML
- Markdown
- DOCX

## Automated Verification

- Test262
- Web Platform Tests (WPT)
- WPT Reftests
- Continuous standards and rendering validation

## Currently in Progress

- HTML and CSS compatibility improvements
- Layout engine refinements
- Cross-platform graphics improvements
- Browser shell improvements
- WebAssembly improvements
- Performance optimization
- Broader device and platform validation

---

# Desktop, Mobile and Web

Broiler is designed so that the same platform components can power multiple deployment models.

The desktop applications run directly on Windows and Linux.

Broiler Browser and Broiler Writer also have Android application heads.

The **Broiler Office Standalone Server (BOSS)** hosts the WebAssembly version of Broiler Writer using ASP.NET Core and Kestrel.

This allows the Writer to run in a browser without depending on a third-party hosted office platform or an external application server.

The long-term goal is not one application tied to one operating system, but reusable infrastructure that can move between desktop, mobile, browser, and self-hosted environments.

---

# Open Infrastructure

Broiler is built around open source, open standards, and replaceable components.

The project deliberately avoids making Chromium, an embedded WebView, or another browser engine a mandatory dependency.

That is not a rejection of those technologies.

It is an exploration of what becomes possible when the browser and document stack itself remains open, inspectable, and under direct control.

This matters for:

- Auditability
- Security review
- Long-term maintainability
- Self-hosting
- Interoperability
- Platform independence
- Avoiding unnecessary dependency on a single browser engine or vendor stack

For organizations that care about digital autonomy, local deployment, or long-lived software infrastructure, these properties can be as important as individual features.

---

# Engineering Principles

## 100% Managed .NET

Every major subsystem is intended to be implemented entirely in managed .NET.

The objective is improved maintainability, portability, auditability, and long-term evolution.

Managed code does not automatically make software secure, but it removes entire categories of unsafe memory-management errors and provides a strong foundation for building understandable infrastructure.

---

## Standards First

Compatibility is measured—not guessed.

Broiler continuously validates itself against industry-standard test suites including:

- Test262
- Web Platform Tests (WPT)
- WPT Reftests

Standards compliance is important not only for compatibility, but also for independence.

Applications should depend on documented standards rather than accidental behavior of one implementation.

---

## Security Through Understandability

Security is not treated as a feature that can be added at the end.

Broiler favors:

- Small, focused components
- Clear trust boundaries
- Managed memory
- Human review
- Automated testing
- Reproducible builds
- Explicit dependencies
- Open source code

A smaller and more understandable software stack is easier to inspect, audit, reason about, and improve.

---

## Shared Platform

Browsers, office applications, desktop software, mobile applications, and WebAssembly deployments should build upon the same reusable infrastructure whenever practical.

Shared components reduce duplication, improve consistency, and simplify long-term maintenance.

---

## Modular Architecture

Large systems become manageable by separating them into focused components with clearly defined responsibilities.

This architecture makes it easier to:

- Replace individual subsystems
- Test components independently
- Review security-sensitive code
- Port the platform
- Reuse infrastructure in new applications

It also makes AI-assisted development significantly more effective while preserving human understanding.

---

## AI-Assisted, Human-Reviewed

AI accelerates implementation.

Humans remain responsible for architecture, review, verification, and quality.

Every accepted contribution is reviewed before becoming part of the platform.

Broiler treats AI as an engineering tool—not as the owner of the codebase.

---

# Why Broiler Exists

Modern browsers and office applications are among the most complex software systems in everyday use.

Despite their different user experiences, they share many of the same underlying technologies:

- Document models
- Styling
- Layout
- Graphics
- Fonts and text shaping
- Input
- Editing
- Runtime services
- Networking
- Scripting

Rather than implementing these foundations multiple times, Broiler explores building them once as reusable managed components.

The goal is not merely to create another browser or another writer.

The goal is to create an open application platform that can support both.

---

# Enhanced Reliability

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

AI can generate code rapidly.

Reliable browser and office infrastructure requires considerably more.

Broiler therefore combines AI-assisted development with modular design, standards compliance, automated verification, and human review.

---

# Why .NET?

Managed runtimes eliminate entire classes of memory-management problems.

Combined with modern tooling, strong refactoring support, cross-platform capabilities, and mature libraries, .NET provides an excellent foundation for building long-lived infrastructure software.

It also allows Broiler to keep large parts of the platform in one language and runtime environment instead of spreading core functionality across multiple native stacks.

That makes the system easier to understand, port, audit, and evolve.

---

# Why Another Browser?

Because browsers are too important to stop experimenting with.

A browser is not merely an application.

It is increasingly an application runtime, document viewer, communication platform, identity boundary, and security boundary.

Broiler investigates whether browser technology can become:

- Easier to understand
- Easier to audit
- Easier to maintain
- More modular
- Less dependent on a single implementation lineage

without abandoning standards compliance.

---

# Why Another Office?

Office software is increasingly infrastructure.

Documents may contain personal information, business knowledge, public-sector data, intellectual property, and long-term records.

Broiler Writer is **not** intended to clone existing office suites.

Instead, it serves as the primary reference implementation for Broiler's shared document platform.

The goal is to make document technology reusable, inspectable, interoperable, and deployable in environments ranging from local desktop applications to self-hosted web systems.

---

# Self-Hosting and Control

Broiler does not assume that every application must depend on an external cloud service.

BOSS demonstrates a different model:

```text
Your Machine / Your Server
          │
          ▼
        BOSS
          │
          ▼
 Broiler Writer (WebAssembly)
          │
          ▼
      Web Browser
```

This enables local or privately hosted deployments while still using a browser-based application model.

Self-hosting is not required—but it should remain possible.

---

# Project Story

Broiler began with a simple question:

> **Can a modern browser be built entirely in managed .NET?**

The common answer was always:

> "Use Chromium."

Broiler's answer remained:

> "No. Entirely in .NET."

Early experiments reused ideas from projects such as **HTML Renderer** and **YantraJS**.

Those experiments demonstrated that a production-quality browser could not simply be assembled from existing components.

The architecture was gradually redesigned into reusable modules.

Automated verification through Test262 and Web Platform Tests became part of the development workflow.

Over time another realization emerged:

A browser and an office suite require many of the same foundational technologies.

That insight transformed Broiler from a browser experiment into a broader application platform.

Today the project is moving from combined development snapshots toward separately versioned Preview Releases and reusable NuGet packages.

---

# Roadmap

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

---

# Getting Started

Interested in Broiler?

- Download the latest Preview Release
- Explore the source code
- Try Broiler Browser
- Try Broiler Writer
- Run the Writer through BOSS
- Explore upcoming NuGet packages
- Report bugs and compatibility problems
- Join the discussions

Feedback and contributions are always appreciated.

---

# Contributing

Contributions of all kinds are welcome.

Please read:

- CONTRIBUTING.md
- CODE_OF_CONDUCT.md
- SECURITY.md

Whether you contribute code, documentation, testing, ideas, interoperability reports, or security analysis, every contribution helps improve the platform.

---

# Acknowledgements

Broiler would not exist without the work of the open-source community.

The project was initially bootstrapped using ideas and code from projects such as **HTML Renderer** and **YantraJS**, both licensed under Apache License 2.0.

Many thanks to their authors and contributors for providing such a strong foundation.

Broiler also depends on the broader ecosystem of open standards, test suites, runtimes, libraries, and developer tools that make independent implementation possible.

---

# License

Broiler is licensed under the **Apache License 2.0**.