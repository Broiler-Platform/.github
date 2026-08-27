# Architecture and Deployment

[← Back to Broiler Platform](https://github.com/Broiler-Platform)

Broiler is designed so that the same platform components can power multiple deployment models — desktop, mobile, browser, and self-hosted.

---

## Platform Layers

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

The browser and writer are the first reference applications built on top of the shared Broiler Platform. BOSS demonstrates how the same document and UI infrastructure can also be deployed through WebAssembly and self-hosted using ASP.NET Core.

---

## Desktop, Mobile and Web

The desktop applications run directly on Windows and Linux. Broiler Browser and Broiler Writer also have Android application heads.

The **Broiler Office Standalone Server (BOSS)** hosts the WebAssembly version of Broiler Writer using ASP.NET Core and Kestrel. This allows the Writer to run in a browser without depending on a third-party hosted office platform or an external application server.

The long-term goal is not one application tied to one operating system, but reusable infrastructure that can move between desktop, mobile, browser, and self-hosted environments.

---

## Self-Hosting and Control

Broiler does not assume that every application must depend on an external cloud service. BOSS demonstrates a different model:

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

Self-hosting is not required — but it should remain possible.

---

## Open Infrastructure

Broiler is built around open source, open standards, and replaceable components. The project deliberately avoids making Chromium, an embedded WebView, or another browser engine a mandatory dependency.

That is not a rejection of those technologies. It is an exploration of what becomes possible when the browser and document stack itself remains open, inspectable, and under direct control.

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

**See also:** [Engineering Principles](https://github.com/Broiler-Platform/.github/blob/main/profile/docs/principles.md) · [Status and Roadmap](https://github.com/Broiler-Platform/.github/blob/main/profile/docs/status.md)
