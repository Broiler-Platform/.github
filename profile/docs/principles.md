# Engineering Principles

[← Back to Broiler Platform](https://github.com/Broiler-Platform)

---

## 100% Managed .NET

Every major subsystem is intended to be implemented entirely in managed .NET. The objective is improved maintainability, portability, auditability, and long-term evolution.

Managed code does not automatically make software secure, but it removes entire categories of unsafe memory-management errors and provides a strong foundation for building understandable infrastructure.

---

## Standards First

Compatibility is measured — not guessed. Broiler continuously validates itself against industry-standard test suites including:

- Test262
- Web Platform Tests (WPT)
- WPT Reftests

Standards compliance is important not only for compatibility, but also for independence. Applications should depend on documented standards rather than accidental behavior of one implementation.

---

## Security Through Understandability

Security is not treated as a feature that can be added at the end. Broiler favors:

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

Large systems become manageable by separating them into focused components with clearly defined responsibilities. This architecture makes it easier to:

- Replace individual subsystems
- Test components independently
- Review security-sensitive code
- Port the platform
- Reuse infrastructure in new applications

It also makes AI-assisted development significantly more effective while preserving human understanding.

---

## AI-Assisted, Human-Reviewed

AI accelerates implementation. Humans remain responsible for architecture, review, verification, and quality.

Every accepted contribution is reviewed before becoming part of the platform. Broiler treats AI as an engineering tool — not as the owner of the codebase.

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

---

**See also:** [Why Broiler](https://github.com/Broiler-Platform/.github/blob/main/profile/docs/why-broiler.md) · [Architecture and Deployment](https://github.com/Broiler-Platform/.github/blob/main/profile/docs/architecture.md)
