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

Just managed .NET, modular architecture, standards compliance, automated verification, AI-assisted engineering, and human review.

Broiler is **not** a wrapper around an existing browser.

It is a reusable platform for building browsers, office applications, and future document-centric software on top of a shared managed runtime.

---

# Platform Snapshot

| Component | Status |
|-----------|--------|
| ECMAScript (Test262) | **>99.99% passing** |
| Web Platform Tests (WPT) | **68% passing** |
| Supported Platforms | Windows, Linux |
| Reference Applications | Browser, Writer, BOSS |
| Document Formats | RTF, HTML, Markdown, DOCX |

---

# Platform Architecture

```
                           Broiler Platform

        ┌──────────────────────────────────────────────────────┐
        │                                                      │
        │ ECMAScript • DOM • CSS • Layout • Graphics           │
        │ UI • Input • Documents • Runtime                     │
        │                                                      │
        └─────────────────────┬────────────────────────────────┘
                              │
          ┌───────────────────┼───────────────────┐
          │                   │                   │
     Browser Desktop     Writer Desktop        WebAssembly
                                                  │
                                                  │
                                                 BOSS
```

The browser, writer, and BOSS are the first reference applications demonstrating how multiple application types can share a common managed platform.

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
- Document model
- Rich text engine
- Platform-independent UI framework
- Platform-independent input abstraction
- Browser runtime
- Office runtime

## Applications

- Broiler Browser
- Broiler Writer
- Broiler Office Standalone Server (BOSS)

## Document Support

- RTF
- HTML
- Markdown
- DOCX

## Automated Verification

- Test262
- Web Platform Tests (WPT)
- Continuous standards validation

## Currently in Progress

- HTML and CSS compatibility improvements
- Layout engine refinements
- Cross-platform graphics backends
- Browser shell improvements
- WebAssembly integration
- Performance optimization

For WebAssembly, Broiler plans to integrate an existing managed .NET runtime such as **WACS**, avoiding unnecessary duplication.

---

# Desktop and Web

Broiler is designed so that the same platform components can power both native desktop applications and WebAssembly deployments.

The **Broiler Office Standalone Server (BOSS)** hosts the WebAssembly version of Broiler Writer using ASP.NET Core and Kestrel, allowing the same application to run locally inside a web browser without requiring an external web server.

The long-term goal is a single platform capable of powering desktop, browser, and cloud-hosted applications.

---

# Engineering Principles

## 100% Managed .NET

Every major subsystem is intended to be implemented entirely in managed .NET.

The objective is improved maintainability, portability, auditability, and long-term evolution.

---

## Standards First

Compatibility is measured—not guessed.

Broiler continuously validates itself against industry-standard test suites including:

- Test262
- Web Platform Tests (WPT)

---

## Shared Platform

Browsers, office applications, desktop software, and WebAssembly deployments should build upon the same reusable infrastructure whenever practical.

Shared components reduce duplication, improve consistency, and simplify long-term maintenance.

---

## Modular Architecture

Large systems become manageable by separating them into focused components with clearly defined responsibilities.

This architecture also enables effective AI-assisted development while preserving human understanding.

---

## AI-Assisted, Human-Reviewed

AI accelerates implementation.

Humans remain responsible for architecture, code review, verification, and quality.

Every accepted contribution is reviewed before becoming part of the platform.

---

# Why Broiler Exists

Modern browsers and office applications are among the most complex software systems in everyday use.

Despite their different user experiences, they share many of the same underlying technologies:

- Document models
- Styling
- Layout
- Graphics
- Text shaping
- Input
- Editing
- Runtime services
- Scripting

Rather than implementing these foundations multiple times, Broiler explores building them once as reusable managed components.

---

# Enhanced Reliability

The **"Enhanced Reliability"** part of the name reflects the project's engineering philosophy.

```
Managed .NET
+ Modular Architecture
+ AI-Assisted Engineering
+ Human Review
+ Automated Standards Testing
--------------------------------------------------
= Enhanced Reliability
```

AI can generate code rapidly.

Reliable browser and office infrastructure requires considerably more.

Broiler therefore combines AI-assisted development with modular design, automated verification, standards compliance, and human review.

---

# Why .NET?

Managed runtimes eliminate entire classes of memory-management problems.

Combined with modern tooling, strong refactoring support, cross-platform capabilities, and mature libraries, .NET provides an excellent foundation for building long-lived infrastructure software.

---

# Why Another Browser?

Because browsers are too important to stop experimenting with.

Broiler investigates whether browser technology can become simpler to understand, easier to maintain, and easier to evolve without sacrificing standards compliance.

---

# Why Another Office?

Broiler Writer is **not** intended to clone existing office suites.

Instead, it serves as the primary reference implementation for Broiler's shared document platform.

Future office applications, editors, and document services are expected to build upon the same reusable infrastructure.

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

---

# Roadmap

Current priorities include:

- Higher WPT compatibility
- HTML and CSS improvements
- Browser shell
- WebAssembly improvements
- Cross-platform graphics
- Office collaboration infrastructure
- PDF support
- Printing
- Performance optimization

---

# Getting Started

Interested in Broiler?

- Download the latest Preview Package
- Explore the source code
- Try Broiler Browser
- Try Broiler Writer
- Host Broiler Writer using BOSS
- Report bugs and suggestions
- Join the discussions

Feedback and contributions are always appreciated.

---

# Contributing

Contributions of all kinds are welcome.

Please read:

- CONTRIBUTING.md
- CODE_OF_CONDUCT.md
- SECURITY.md

Whether you contribute code, documentation, testing, ideas, or discussions, every contribution helps improve the platform.

---

# Acknowledgements

Broiler would not exist without the work of the open-source community.

The project was initially bootstrapped using ideas and code from projects such as **HTML Renderer** and **YantraJS**, both licensed under Apache License 2.0.

Many thanks to their authors and contributors for providing such a strong foundation.

---

# License

Broiler is licensed under the **Apache License 2.0**.
