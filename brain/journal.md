# Journal

Append-only changelog of notable changes. Newest first, dated `YYYY-MM-DD`. One
or two lines each; link to a decision or PR when relevant. This is the
co-evolution trail — what changed, and where to read why.

---

- **2026-06-12** — Positioning fix: the **product** is **framework-agnostic**
  (decoupled from the training framework), not "tool-agnostic". "Tool-agnostic"
  now refers only to the co-evolve `brain/`/dev process (works with any AI coding
  assistant) and is kept out of product-facing docs (README, pyproject).

- **2026-06-12** — Bootstrapped project foundation (Milestone 0) with an
  intentionally **minimal** toolchain: `uv` project management (`pyproject.toml`),
  importable `camel_env` package, `pytest` smoke tests, `ruff` lint+format, GitHub
  Actions CI (py3.10 + 3.13), and community docs (README with badges, CONTRIBUTING,
  fleshed-out roadmap). `mypy`/coverage/`pre-commit`/`py.typed` and a wider Python
  matrix deliberately deferred — see [decisions.md](decisions.md) and
  [open-questions.md](open-questions.md).

- **2026-06-12** — Established the `brain/` long-term memory: workflow contract,
  conventions, architecture, glossary, and append-only decisions/journal/
  open-questions. Root `CLAUDE.md` reduced to a pointer.
  See [decisions.md](decisions.md).
