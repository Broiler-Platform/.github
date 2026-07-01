# Broiler Platform

> **Browser and Office Infrastructure in Intermediate Language with Enhanced Reliability**

## Hi there 👋

Welcome to the **Broiler Platform**!

Broiler is an open-source platform project with an ambitious long-term goal:

> **Build a production-ready browser and office platform entirely in managed .NET.**

The project combines practical software engineering with ongoing research into browser engines, document rendering, AI-assisted engineering, and modular platform design.

No native browser engine.

No Chromium.

No embedded WebView.

Just .NET.

> **Broiler combines AI-assisted engineering with rigorous human review and automated testing.**

---

# Vision

Modern browsers and office suites are among the largest and most complex software systems ever built.

Broiler explores whether a different engineering approach is possible:

* 100% managed .NET
* Modular architecture
* AI-assisted engineering
* Human-reviewed changes
* Extensive automated testing
* Shared infrastructure for browser and office applications

The goal is not simply to build *another browser*.

The goal is to build a reusable platform for document rendering, scripting, layout, graphics, and user interaction that can power both browsers and office applications.

---

# Why "Enhanced Reliability"?

The **"Enhanced Reliability"** part of the name describes the engineering philosophy behind Broiler.

The project is developed with extensive AI assistance. AI accelerates implementation, while human review, automated testing, and a modular architecture help improve correctness, maintainability, and long-term reliability.

Keeping the codebase clean, modular, and well-structured also makes it easier for AI to understand and contribute effectively despite today's limited context windows.

AI is rapidly becoming an important tool in cybersecurity—for both attackers and defenders. For software such as browsers and office applications, careful AI-assisted development combined with rigorous human review is therefore an important part of the engineering process.

In short:

> **Managed .NET + AI-assisted engineering + Human review + Automated verification = Enhanced Reliability**

---

# The Story Behind Broiler

I'm an enthusiastic .NET developer (before that C++, C, Pascal, Windows Batch, C64 BASIC... and, before all of that, learning to read and write my native language 😄).

For many years I kept asking myself a simple question:

> *Is it possible to build a modern browser entirely in .NET?*

When AI became capable enough to assist with software development, I naturally asked:

> "Build me a browser in .NET."

The answer was always the same:

> "Use Chromium."

My answer never changed:

> "No. Entirely in .NET."

Without an existing code base, the conversation usually ended there.

Eventually I discovered two impressive open-source projects: **HTML Renderer** and **YantraJS**.

At first the idea looked deceptively simple:

> Combine both projects, add a little WPF... browser finished!

As you might expect, it wasn't.

The browser couldn't pass the ACID tests.

Google didn't work.

Gmail didn't work.

And asking AI to *"make Google work"* didn't magically solve the problem either.

Instead of patching the existing code, I started rebuilding the architecture piece by piece.

Both projects were gradually refactored into much smaller and more focused components. AI became an accelerator rather than the architect.

Automated **Test262** and **Web Platform Tests (WPT)** runners were integrated into GitHub, allowing AI to continuously work on isolated issues while every accepted change remained under human control.

Four months later, the JavaScript engine successfully passed the complete Test262 suite.

While one AI focused on ECMAScript, another helped modernize the HTML runtime. It only took a few minutes of discussion to organize an architecture that I already had roughly in mind.

A browser naturally consists of only a handful of major building blocks:

* DOM
* CSS
* Layout
* Graphics
* Runtime

The interesting realization came afterwards.

An office suite requires almost exactly the same infrastructure.

At that point the project's vision expanded from **Browser Infrastructure** to **Browser and Office Infrastructure**—which is what **Broiler** stands for today.

---

# Current Status

The project is under active development and is **not yet intended for production use**.

Already implemented:

* ✅ ECMAScript / JavaScript engine
* ✅ Large parts of the HTML runtime
* ✅ Automated Test262 integration
* ✅ Automated Web Platform Tests (WPT) infrastructure

Currently in progress:

* 🚧 CSS engine improvements
* 🚧 Layout engine
* 🚧 Cross-platform graphics backends
* 🚧 Browser shell
* 🚧 Office document infrastructure

For WebAssembly there is already an excellent third-party engine written entirely in .NET (**WACS**), which is planned for integration instead of reinventing the wheel.

---

# Design Principles

Broiler follows a small set of engineering principles.

### 100% Managed .NET

Every major subsystem is written entirely in managed .NET.

### AI-Assisted Engineering

AI is a development tool—not the maintainer.

### Human Review

Every accepted change is reviewed and approved by a human.

### Modular Architecture

Large systems become understandable by breaking them into small, independent components.

### Standards First

Whenever practical, Broiler follows existing web standards instead of inventing new ones.

### Test-Driven Compatibility

Interoperability is measured—not guessed.

Test262 and Web Platform Tests are first-class citizens throughout the project.

### Browser and Office Together

Browsers and office suites share much more infrastructure than they appear to.

Broiler aims to build these foundations once and reuse them everywhere.

---

# Supported Platforms

In principle, every platform supported by **.NET 10** should also be supported by Broiler.

The current graphics backend and input system are implemented using **Direct2D on Windows**, but the architecture is intentionally platform-independent.

Additional backends for Linux, macOS, Android and other platforms are planned.

---

# Changelog

## 2026-07-01 — First Preview

### Highlights

* More than **99.99%** of the Test262 suite passes successfully (approximately **53,194** tests).
* More than **50%** of the CSS Web Platform Tests currently render correctly.
* Automated Test262 and WPT integration.
* Windows frontend based on Direct2D.

### Notes

ACID tests are no longer a primary compatibility target, as the Web Platform Tests provide significantly broader and more modern standards coverage.

---

# Roadmap *(subject to change)*

## Next Preview

* Improved Web Platform Test compatibility
* UI improvements
* Expanded human review coverage
* First preview of **Broiler Writer**

## Future Milestones

* Cross-platform graphics backends
* Browser shell improvements
* Office document model
* Rich text editing
* Additional HTML and CSS compatibility
* WebAssembly integration
* Performance optimizations

## Long-Term Goals

* Complete platform independence

  * Windows
  * Linux
  * Android
  * macOS
  * iOS
* Standards-compliant browser platform
* Modern office platform built on the same infrastructure

---

# Why another browser?

Because browsers are among the most important applications we use every day.

They deserve continuous experimentation.

Broiler investigates whether a browser written entirely in managed .NET can improve maintainability, auditability, portability, and AI-assisted development without sacrificing standards compliance.

---

# Why another office suite?

Modern browsers and office suites share surprisingly similar foundations:

* Document models
* Styling
* Layout
* Graphics
* Fonts
* Scripting
* Runtime services

Instead of implementing these systems twice, Broiler explores building one shared platform capable of supporting both.

---

# Why .NET?

Managed runtimes eliminate entire classes of memory-management problems and allow developers to focus on architecture instead of low-level infrastructure.

They also make large-scale refactoring significantly easier—an important advantage for a modular architecture developed with extensive AI assistance.

Broiler exists to explore how far this engineering approach can go.

---

# Acknowledgements

Broiler would not exist without the excellent work of many open-source developers.

The project was initially bootstrapped using ideas and code from projects such as **HTML Renderer** and **YantraJS**, both licensed under Apache 2.0.

Over time, the architecture has been extensively refactored, modularized, and expanded into a new platform.

Many thanks to the authors and contributors of these projects for providing such a strong foundation.

---

# Why the name "Broiler"?

The name wasn't planned.

I was looking for a memorable acronym involving **Browser**, **.NET**, and **Intermediate Language**, which eventually led to **Broiler**.

Only afterwards did I remember the German word *"Broiler"* (roast chicken), which brought back childhood memories.

I liked the name.

The acronym came afterwards. 😄

---

# Why is the logo a chicken using a laptop?

Because the project is called **Broiler**.

And because a friendly chicken working on a laptop felt like the perfect mascot for a browser and office platform. 🐔💻
