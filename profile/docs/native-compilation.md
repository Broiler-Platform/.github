# Native Compilation

[← Back to Broiler Platform](https://github.com/Broiler-Platform)

Broiler is written entirely in managed .NET. That invites a fair question: does a managed browser and office stack pay a permanent performance and deployment tax against native code?

The project's answer is **NativeAOT** — publishing ahead-of-time compiled, self-contained native binaries. A NativeAOT build has no .NET runtime dependency, no JIT warm-up, and no framework installation step. The user runs a single executable.

The goal is to close the gap between "implemented in managed .NET" and "ships and performs like a native application" — without giving up any of the properties that made managed .NET the choice in the first place.

---

## AOT is an architectural constraint, not a publish flag

This is the part that matters most, and the reason NativeAOT shows up in the platform's design rather than only in its build scripts.

NativeAOT compiles the whole program ahead of time. There is no runtime code generation and no runtime type discovery. Anything that resolves behavior by name at runtime — reflection over types the compiler cannot see, `Activator.CreateInstance`, reflection-based serialization, plug-in discovery by scanning assemblies — either fails to work or silently defeats trimming.

Two consequences run through the codebase:

- **A component that is AOT-compatible stays that way only if it is kept that way.** Reflection introduced into an AOT-published component will break the publish while leaving an ordinary build perfectly green. This is why CI publishes with AOT rather than only building.
- **Composition must be explicit.** Back ends and language profiles are *registered* through direct, typed references — never discovered by assembly or type name. Static, source-generated catalogs replace plug-in scanning. There is no binary plug-in ABI.

The second point is what connects NativeAOT to the platform architecture: the same rule that makes an AOT publish possible also makes the dependency graph inspectable, which is a property the project wants for its own sake.

---

## Where it stands

| Target | Native compilation | Status |
|---|---|---|
| **Writer — Windows desktop** (`win-x64`) | NativeAOT | ✅ Shipping |
| **Writer — Linux desktop** (`linux-x64`) | NativeAOT | ✅ Shipping |
| **Broiler.JS** | NativeAOT | 🚧 In progress — AOT sample exists, zero-warning gate open |
| **Broiler.VM** and its language profiles | NativeAOT-compatible by design | 📋 Planned — not started |
| **Android heads** | — | ❌ Excluded — experimental upstream |
| **WebAssembly** | Not NativeAOT (see below) | ❌ Not applicable |

---

## Broiler Writer — shipping today

The two desktop heads of Broiler Writer publish with NativeAOT. The `win-x64` and `linux-x64` artifacts are **a single self-contained native binary that runs with no .NET runtime installed** — 9.2 MB for the Windows head, against a 162-file framework-dependent drop.

It publishes cleanly rather than by suppression: an AOT publish of the Windows head reports **zero `IL2xxx`/`IL3xxx` warnings**, and the Linux head reports zero under the trim, AOT, and single-file analyzers.

That is possible because nothing in the Writer's dependency closure needs reflection the compiler cannot see through. The notable case is the Windows graphics backend: it dispatches COM through manual vtable offsets and `delegate* unmanaged` function pointers rather than `ComImport` interfaces — which is the one pattern that would otherwise rule out an AOT publish of the Direct2D path.

A framework-dependent build remains available for anyone who wants one.

---

## Broiler.JS — in progress

Extending native compilation to JavaScript execution is under way in [`Broiler.JS`](https://github.com/Broiler-Platform/Broiler.JS). A `Broiler.JavaScript.NativeAotSample` sets `PublishAot=true` today, and the gate the work is measured against is that it must publish with **zero trim and AOT warnings and then execute a representative workload** — not merely compile.

The blocking work is architectural rather than cosmetic: legacy name-based assembly probing has to be retired, because resolving a back end or a language profile by name defeats both trimming and AOT. It is treated as a blocker rather than as cleanup for that reason.

Native compilation also reaches into the engine's own design decisions. `InvariantGlobalization=true` under NativeAOT is part of why some of the specification surface is implemented directly rather than delegated to platform libraries.

---

## Broiler.VM — planned

[`Broiler.VM`](https://github.com/Broiler-Platform/Broiler.VM) is a planned NativeAOT-compatible component that executes verified bytecode artifacts.

> [!IMPORTANT]
> Broiler.VM is **a component plan, not an implementation**. Its milestones are recorded as not started, and no capability should be inferred from planning text. The repository's own status ledger is the authority.

The design idea is that Broiler.VM is a **host for language profiles, rather than a language itself**. The core owns profile selection, bounded artifact loading, the verified-artifact boundary, the execution lifecycle, resource limits, cancellation, and diagnostics. It deliberately owns no opcode set, no value representation, and no language semantics — those belong to the profiles.

Two profiles are intended first: **JavaScript** and **WebAssembly**. Profiles reference the core; the core never references a profile, and a profile is added by compiling it in and registering its descriptor directly. No assembly scanning, no loading types by name, no runtime extension directory, no binary plug-in ABI — all of which follow from the NativeAOT contract described above.

This is also the answer to an obvious objection. A JavaScript engine normally reaches for a JIT, and a NativeAOT program cannot generate code at runtime. A verified bytecode interpreter with language profiles is the route that keeps dynamic-language execution inside the AOT contract.

---

## What "WebAssembly" means here

The word appears in two unrelated places in Broiler, which is worth untangling:

- **WebAssembly as a deployment target** — Broiler Writer compiled to run in a browser and served by [BOSS](https://github.com/Broiler-Platform/.github/blob/main/profile/docs/architecture.md). This is **not** NativeAOT. NativeAOT emits a native binary for a desktop operating system and does not apply to a browser target at all; the WebAssembly analogue is a separate mono feature.
- **WebAssembly as a guest bytecode** — a planned Broiler.VM *profile*, where the VM executes wasm bytecode as input, in the same way it would execute JavaScript bytecode.

The first is how Broiler ships to browsers. The second is a planned execution capability. They are different mechanisms that happen to share a name.

Android is excluded separately: the Android SDK reports NativeAOT on Android as an experimental feature not yet suitable for production, and it conflicts with that head's untrimmed build, since native compilation implies trimming.

---

## For contributors

If you work on a component that publishes with NativeAOT, or one that is being moved toward it, the practical rules are:

- Do not introduce reflection, `Activator.CreateInstance`, or reflection-based serialization into an AOT-published closure. An ordinary build will not tell you that you broke it.
- Register components explicitly through typed references. Do not resolve them by assembly or type name.
- Treat trim and AOT analyzer warnings as failures rather than noise.

See [Contributing](https://github.com/Broiler-Platform/.github/blob/main/CONTRIBUTING.md) for the general contribution process.

---

**See also:** [Architecture and Deployment](https://github.com/Broiler-Platform/.github/blob/main/profile/docs/architecture.md) · [Engineering Principles](https://github.com/Broiler-Platform/.github/blob/main/profile/docs/principles.md) · [Status and Roadmap](https://github.com/Broiler-Platform/.github/blob/main/profile/docs/status.md)
