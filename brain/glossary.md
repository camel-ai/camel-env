# Glossary

Domain vocabulary for `camel-env`. Living doc — add or refine terms as they're
introduced. Keep definitions one or two sentences.

- **Environment** — the core unit, a triplet `(instruction, sandboxes,
  verification/reward_fn)`. See [architecture.md](architecture.md).
- **Instruction** — the task/prompt given to an agent within an environment.
- **Sandbox** — an isolated execution context where an instruction is carried
  out; provided/managed by a runtime.
- **Runtime** — the machinery that creates and runs sandboxes.
- **Verifier** — logic that checks whether the agent satisfied the instruction.
- **Reward function (`reward_fn`)** — produces a (typically scalar) reward signal
  from an outcome; the training-facing form of verification.
- **Agent** — an actor that operates within an environment to satisfy the instruction.
- **Model** — the backend powering an agent.
- **Dataset (of environments)** — a collection of environments to train or evaluate on.
- **Environment-as-service** — exposing environments over a service boundary so
  training/eval frameworks consume them without coupling.
- **Co-evolution** — the practice of evolving the repo and the AI tool together,
  tool-agnostically; the brain folder is its concrete mechanism here.
