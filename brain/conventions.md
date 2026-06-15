# Conventions

Code and repo conventions. Stronger than guidance, softer than a law of physics:
deviate only with a recorded reason ([decisions.md](decisions.md)). This is a
living doc — edit in place to keep it true.

## Project shape
- Python package: `camel_env/` (see [architecture.md](architecture.md) for module roles).
- Configuration is **declarative**: behavior is driven by YAML, not hardcoded.
  New components should be selectable/wireable from config.
- The environment must stay **framework-agnostic** — decoupled from any training
  framework. (Tool-agnosticism toward AI coding assistants is a property of the
  co-evolve `brain/`/dev process, not the product — don't conflate the two.)

## ✅ Do
- Put code in the module that owns its responsibility (reward → `verifiers/`,
  sandbox/execution → `runtimes/`, serving → `services/`, etc.).
- Make new agents, reward functions, and sandboxes pluggable and config-driven.
- Add type hints to public functions and classes.
- Write a test alongside new behavior; the roadmap targets production-grade tests
  and CI ([open-questions.md](open-questions.md)).
- Keep public interfaces small and stable; document the *why* in docstrings.

## ❌ Don't
- Don't couple environment logic to a specific trainer or a specific AI tool.
- Don't bypass the config layer by hardcoding component choices.
- Don't add dependencies without a recorded reason.
- Don't leave the brain stale after a structural change.

## Tooling (established 2026-06-12) — intentionally minimal
- **Env & deps:** `uv` (`uv sync`, `uv add`, `uv run`). Lockfile `uv.lock` is committed.
- **Build backend:** `hatchling`. Package config in [pyproject.toml](../pyproject.toml).
- **Lint + format:** `ruff` (`uv run ruff check .`, `uv run ruff format .`).
- **Tests:** `pytest` in `tests/`, named `test_*.py` (`uv run pytest`).
- **Python floor:** `>=3.10` (floor only, not a cap); CI tests 3.10 + 3.13.
- **Deps:** unpinned for now; pin lower bounds only on real incompatibility.
- **Commits:** Conventional Commits prefixes (`feat:`, `fix:`, `docs:`, …).
- **Merging:** branch off `main`, PR, green CI + 1 review, **squash-merge**.

**Deliberately minimal** — only `ruff` + `pytest`. Type checking (`mypy`) and
coverage (`pytest-cov`) are intentionally out; `pre-commit` may be added later.
Still add type hints to public APIs by hand — it's good practice regardless.

See [decisions.md](decisions.md) for the reasoning behind these choices.
