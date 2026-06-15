# Decisions

Append-only, ADR-style log. Capture the *why* and the rejected alternatives —
the code shows the *what*. Newest first. Don't edit past entries; to reverse a
decision, add a new entry that supersedes it.

### Template
```
### YYYY-MM-DD — <short title>
**Context:** what prompted this.
**Decision:** what was chosen.
**Why:** reasoning; alternatives rejected.
**Supersedes:** <date/title>, if any.
```

---

### 2026-06-12 — uv + hatchling for project & dependency management
**Context:** The project is public/community-facing and needs an easy, reproducible
setup so contributors can create an env, install deps, and install the package
with minimal friction.
**Decision:** Use `uv` for environment + dependency management (`pyproject.toml`
+ `uv.lock`, `uv sync`), with `hatchling` as the build backend. Dev tools live in
a `[dependency-groups] dev` group.
**Why:** `uv` is fast, reproducible (lockfile), and a single `uv sync` replaces
manual venv/pip steps. Hatchling is uv's modern default backend. Alternatives
rejected: bare pip+venv (no lockfile, slower), poetry (heavier, slower).

### 2026-06-12 — Minimal tooling & CI baseline
**Context:** Need engineering hygiene before much code exists (Milestone 0), but
without imposing friction while the API is still in flux.
**Decision:** Start with the **bare minimum**: `ruff` (lint + format) and `pytest`
(tests) — the two "regulations" we care about (format + test). GitHub Actions CI
runs ruff + pytest on Python **3.10 and 3.13** (floor + latest) for every PR.
Squash-merge + green CI + 1 review on `main`. Conventional Commits. Python floor
`>=3.10` (a floor, not an upper cap). Dependency versions left **unpinned** for now.
**Deliberately deferred** (added later as the codebase matures, see
[open-questions.md](open-questions.md)): `mypy` (types), `pytest-cov` (coverage
gate), `pre-commit` hooks, and a wider Python test matrix.
**Why:** Type checking and coverage gates create churn when interfaces change
daily; better to add them once the core stabilises. Unpinned deps reduce early
maintenance; pin lower bounds only when a real incompatibility appears.
**Supersedes:** the earlier same-day "Tooling & CI baseline" intent (which
included mypy/pytest-cov/pre-commit/4-version matrix from the start).

### 2026-06-12 — Brain folder as the co-evolution mechanism
**Context:** The project aims to co-evolve the repo with AI tools, tool-agnostically
([architecture.md](architecture.md)). Root `CLAUDE.md` is auto-loaded but should
stay thin.
**Decision:** Keep `CLAUDE.md` as a thin pointer; store all durable memory in
`brain/`, split into a workflow contract, living docs (conventions, architecture,
glossary), and append-only records (decisions, journal, open-questions).
**Why:** A single growing `CLAUDE.md` becomes unreadable and tool-specific.
A structured, plain-Markdown brain is tool-agnostic and lets memory co-evolve
with code. Alternative rejected: keeping everything in `CLAUDE.md`.

### 2026-06-12 — Environment defined as a triplet, decoupled from training
**Context:** Need a stable abstraction between training frameworks and varied
environment datasets ([docs/design.md](../docs/design.md)).
**Decision:** Model an environment as `(instruction, sandboxes,
verification/reward_fn)`, configurable via YAML, served as a service, decoupled
from any specific trainer and agnostic to any specific AI tool.
**Why:** Decoupling enables unified training/eval and reuse across datasets and
tools. Foundational to the project; recorded here as the baseline.
