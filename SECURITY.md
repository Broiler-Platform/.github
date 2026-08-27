# Security Policy

This policy applies to all repositories in the [Broiler-Platform](https://github.com/Broiler-Platform) organization, including every platform component repository (`Broiler.JS`, `Broiler.CSS`, `Broiler.HTML`, `Broiler.DOM`, `Broiler.Graphics`, `Broiler.UI`, `Broiler.Input`, `Broiler.Media`, `Broiler.Documents`, `Broiler.Browser`, `Broiler.Writer`, and the components nested beneath them).

---

## Preview status — please read first

> [!IMPORTANT]
> Broiler is a **first-preview** project. It is **not production-ready, not security-audited, and not a sandbox.**

Broiler implements a browser engine, a JavaScript engine, image codecs, and document parsers — all of which process complex, attacker-controllable input. In a mature browser these components are hardened and sandboxed. **In Broiler they are not yet.**

Specifically, and by the project's own [human review records](https://github.com/Broiler-Platform/Broiler/blob/main/HUMAN_REVIEW.md):

- JavaScript execution and host integration are security-sensitive and **do not constitute a sandbox**. Script does not run inside a security boundary.
- Renderer paths are **not hardened against hostile HTML and CSS**.
- Image codecs, other untrusted binary input, and native platform interop are security-sensitive areas under active review.
- Several components remain **pending review** rather than approved.

**Use Broiler only with controlled, non-hostile input**, unless the host application provides its own isolation. Do not use it to render untrusted web content in a security-sensitive context.

---

## Reporting a vulnerability

**Please do not report security issues in public issues, pull requests, or discussions.**

Report privately through GitHub Security Advisories:

**➜ [Open a private security report](https://github.com/Broiler-Platform/Broiler/security/advisories/new)**

Use that form for **any** Broiler repository, including the component submodules — reports for all of them are triaged in one place. Only you and the maintainers can see the report.

### What to include

The more of this you can provide, the faster a report can be confirmed:

- The affected component and version, release, or commit SHA
- Platform and configuration (Windows / Linux / Android / WebAssembly via BOSS)
- A minimal reproducer — an HTML, CSS, JavaScript, or document file that triggers the issue
- What happens, and what you expected instead
- Any crash output, stack trace, or log
- Your assessment of the impact

### What to expect

This is a small project, so please allow for a volunteer response time:

| Stage | Target |
|-------|--------|
| Acknowledgement of your report | within 7 days |
| Initial assessment | within 30 days |
| Fix or documented mitigation | depends on severity and scope |

You will be credited in the advisory unless you ask not to be.

---

## Scope

Because Broiler is an unhardened preview, the useful distinction is not "is this a bug in a security-sensitive component" — much of the engine is — but "does this behave worse than the documented preview limits."

### In scope

- Anything that affects users of a **published Preview Release binary**
- Memory-safety issues, including those reachable through `unsafe` code or native platform interop
- Code execution, file system access, or network access reaching **outside** the process from content that should not have it
- Same-origin policy or other web security boundary failures **that the engine claims to implement**
- Issues in BOSS that expose the host machine, other users' documents, or the server beyond what the deployment intends
- Credential, token, or secret leakage
- Dependency vulnerabilities with a demonstrated impact on Broiler

### Out of scope

These are known and documented consequences of the preview status. They are valuable as **[bug reports](https://github.com/Broiler-Platform/Broiler/issues)** — just not as security reports:

- Crashes, hangs, or unbounded memory use when rendering hostile or malformed HTML, CSS, JavaScript, images, or documents
- Script escaping "the sandbox" — there is no sandbox
- Missing hardening or defense-in-depth measures that a mature browser has and Broiler does not yet
- Rendering or standards-compliance differences from other browsers
- Findings from automated scanners without a demonstrated, reachable impact
- Issues in the third-party test suites (Test262, Web Platform Tests) themselves

If you are unsure which side a finding falls on, report it privately and let the maintainers decide.

---

## Supported versions

| Version | Supported |
|---------|-----------|
| Latest [Preview Release](https://github.com/Broiler-Platform/Broiler/releases) | ✅ |
| `main` branch | ✅ |
| Earlier previews and development snapshots | ❌ |

Fixes land on `main` and reach users in the next Preview Release. There are no long-term support branches, and prior previews are not patched.

---

## Disclosure

Broiler follows coordinated disclosure. Please give the maintainers a reasonable opportunity to ship a fix before publishing details — 90 days is the usual expectation, shorter if a fix ships sooner, and negotiable if an issue is being actively exploited.

Fixed issues are published as GitHub Security Advisories on the affected repository.
