# Native Compilation

[← Back to Broiler Platform](https://github.com/Broiler-Platform)

Updated against the aggregate checkout on **23 October 2026**.

NativeAOT publishes managed .NET applications as native executables without requiring an installed .NET runtime. Deployment can still include operating-system libraries, content and other files; a publish setting alone does not prove a single-file distribution, artifact size, warning count or release acceptance.

## Current publish paths

| Target | Repository evidence |
|---|---|
| Writer Windows x64 / Linux x64 | NativeAOT publish and CI paths; framework-dependent variants also exist |
| Plate Windows x64 | NativeAOT publish path |
| Mail Windows x64 / ARM64 | NativeAOT self-contained and framework-dependent validation packages; unsigned builds and draft releases |
| Android application heads | Separate Android workload and publish path; not the desktop NativeAOT path |
| Writer WebAssembly | Browser deployment through BOSS; distinct from desktop NativeAOT |
| Broiler.VM | NativeAOT host/composition work exists; milestones and support remain unaccepted |

These are source declarations and component documentation, not results from a fresh publish in this update. See the component workflows for configurations and prerequisites: [Writer](https://github.com/Broiler-Platform/Broiler.Writer/tree/main/.github/workflows), [Plate](https://github.com/Broiler-Platform/Broiler.Plate/tree/main/.github/workflows), [Mail](https://github.com/Broiler-Platform/Broiler.Mail/tree/main/.github/workflows).

## Composition constraints

NativeAOT requires code and metadata needed at runtime to remain available after trimming. Unbounded reflection, runtime code generation and assembly scanning can violate that contract. Use direct typed registration and source-generated serialization where appropriate; reflection supported by explicit metadata is not categorically forbidden. Validate the actual publish closure with trim and AOT analyzers, rather than relying on an ordinary build.

JSEAL keeps contracts separate from the engine-specific providers. A composition root selects a provider explicitly. The presence of an engine provider in a component repository does not make that component's contracts assembly engine-dependent.

## Broiler.VM implementation and acceptance

[Broiler.VM](https://github.com/Broiler-Platform/Broiler.VM) owns a profile-neutral core and profile project families within the same component. The core owns bounded loading, verification, lifecycle, resource authority and diagnostics; JavaScript and WebAssembly profiles own language execution. Profiles are compiled in and registered explicitly, without assembly scanning or a binary plug-in ABI.

The checkout contains bytecode execution, a WebAssembly decoder/validator/interpreter and native artifact execution work. JavaScript defaults to bytecode. General native output may call interpreter handlers; restricted numeric programs have a direct machine-code path subject to admission rules. Executable backends are x86-64 with Windows or System V conventions; ARM64 is emitting-only.

All VM-0 through VM-7 milestones remain **in progress and unaccepted**. The [status ledger](https://github.com/Broiler-Platform/Broiler.VM/blob/main/docs/roadmap.status.md) and [JavaScript execution-mode record](https://github.com/Broiler-Platform/Broiler.VM/blob/main/src/Broiler.VM.Profile.JavaScript/docs/roadmap.backends.md) define the evidence and limits. Compiling a VM host with NativeAOT does not itself compile guest JavaScript into machine code.

The declared graph now includes a VM → Broiler.JS reference. Browser VM configurations select an optional provider while HtmlBridge DOM bindings still reach Broiler.JS; the current implementation is not an engine-independent replacement of that entire closure.

## Two uses of WebAssembly

- **Deployment target:** Writer runs inside a user browser, with assets served by BOSS.
- **Guest format:** Broiler.VM's WebAssembly profile loads and interprets wasm input. It exists in source but has no accepted support claim.

See [Architecture](architecture.md), [Component Map](component-map.md), and [Contributing](https://github.com/Broiler-Platform/.github/blob/main/CONTRIBUTING.md).
