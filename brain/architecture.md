# Architecture

The current design and module map. Living doc — keep it accurate as the system
evolves. Source of intent: [docs/design.md](../docs/design.md).

## Core idea
`camel-env` is an **environment-as-a-service** layer that sits between training
frameworks and datasets of environments.

An **environment** is a triplet:

```
environment = (instruction, sandboxes, verification / reward_fn)
```

See [glossary.md](glossary.md) for each term.

## Design aims (from docs/design.md)
1. Serve as the middleman between training frameworks and diverse environment datasets.
2. Make agents, reward functions, and sandboxes customizable.
3. Make everything configurable via YAML.
4. Unify training and evaluation under one interface.
5. Run the environment as a service.
6. **Co-evolve the repo and the AI tool (claude/codex), agnostic to the specific
   tool.** ← this brain folder is the project's expression of that aim.

## Module map (`camel_env/`)
> Modules currently exist as empty packages — this map records intended
> responsibility. Update each entry as real code lands.

| Module | Responsibility |
|--------|----------------|
| `environments/` | Environment definitions — assembling the (instruction, sandbox, verifier) triplet. |
| `dataset/` | Loading and managing datasets of environments. |
| `agents/` | Agent abstractions that act within environments. |
| `models/` | Model interfaces / backends used by agents. |
| `runtimes/` | Sandbox & execution runtimes where instructions are carried out. |
| `verifiers/` | Verification logic and reward functions. |
| `services/` | The service layer exposing environments (environment-as-service). |
| `utils/` | Shared helpers. Keep thin; prefer the owning module. |

## Key properties to preserve
- **Framework-agnostic:** the environment knows nothing about the trainer
  (decoupled from any training framework). This is the product's defining trait.
- **Config-first:** components are wired through YAML.

> Note: "tool-agnostic" / co-evolving with any AI coding tool (claude/codex) is a
> property of the **dev process and this `brain/`**, not of the product runtime.
> Don't surface it as a product feature. See [glossary.md](glossary.md).

When any of these change, record it in [decisions.md](decisions.md).
