# Roadmap

Where `camel-env` is headed and in what order. This is a living plan — dates are
intentionally omitted; we ship by milestone, not by deadline. Decisions behind
these items are recorded in [`../brain/decisions.md`](../brain/decisions.md);
open unknowns live in [`../brain/open-questions.md`](../brain/open-questions.md).

Legend: ✅ done · 🚧 in progress · ⬜ planned

## Milestone 0 — Project foundation (engineering hygiene)
The scaffolding that makes the project safe to build on and easy to contribute to.

- ✅ `uv`-based project management (`pyproject.toml`, reproducible `uv sync`)
- ✅ Package skeleton importable (`import camel_env`)
- ✅ Linting + formatting (`ruff`)
- ✅ Test runner (`pytest`) + first smoke tests
- ✅ CI on every PR (GitHub Actions, Python 3.10 + 3.13)
- ✅ Contributor docs (`README`, `CONTRIBUTING`, `brain/`)
- ⬜ Branch protection on `main` (require CI + 1 review + squash)
- ⬜ Pre-commit hooks
- ⬜ Issue / PR templates

> Further milestones (core abstractions, environment-as-service, release,
> community hardening) will be added here once Milestone 0 is complete and the
> direction is firmed up. Design intent lives in [design.md](design.md).

---

### How to update this roadmap
When you complete an item, flip its box to ✅ and add a line to
[`../brain/journal.md`](../brain/journal.md). When scope changes, edit here and
record the reasoning in [`../brain/decisions.md`](../brain/decisions.md).
