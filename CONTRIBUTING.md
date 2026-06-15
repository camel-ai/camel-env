# Contributing to camel-env

Thanks for your interest in contributing! This guide covers local setup, the
development workflow, and our rules for tests, reviews, and merging. It is the
public-facing summary of [`brain/workflow.md`](brain/workflow.md) and
[`brain/conventions.md`](brain/conventions.md).

## 1. Local setup

We use [**uv**](https://docs.astral.sh/uv/) for environment and dependency
management. [Install uv](https://docs.astral.sh/uv/getting-started/installation/),
then:

```bash
git clone https://github.com/camel-ai/camel-env.git
cd camel-env
uv sync                         # create .venv, install package + dev tools
```

`uv sync` reads [pyproject.toml](pyproject.toml) and the locked `uv.lock` to give
everyone the **exact same dependency versions** — reproducible by construction.

### Common commands

| Task | Command |
|------|---------|
| Run tests | `uv run pytest` |
| Lint | `uv run ruff check .` |
| Auto-fix lint | `uv run ruff check --fix .` |
| Format | `uv run ruff format .` |
| Add a runtime dependency | `uv add <pkg>` |
| Add a dev dependency | `uv add --dev <pkg>` |

> We keep the toolchain minimal on purpose — just **ruff** (lint + format) and
> **pytest** (tests). Other checks may be added as the codebase matures — see
> [`brain/open-questions.md`](brain/open-questions.md).

## 2. Development workflow

We follow **Orient → Change → Verify → Record** (see
[`brain/workflow.md`](brain/workflow.md)):

1. **Branch off `main`.** Never commit to `main` directly.
   - Branch names: `feat/...`, `fix/...`, `docs/...`, `chore/...`, `test/...`.
2. **Make a focused change.** One logical concern per PR.
3. **Verify locally:** `uv run pytest`, `uv run ruff check .`, `uv run ruff format .`.
4. **Record:** update docs and the relevant `brain/` file in the same change
   (e.g. a design decision → [`brain/decisions.md`](brain/decisions.md)).

## 3. Tests

- **Every new feature ships with tests.** A bug fix includes a test that would
  have caught the bug.
- Tests live in `tests/`, named `test_*.py`, run with `pytest`.
- CI runs the suite on Python 3.10 and 3.13. **A red CI blocks merge.**
- Aim for meaningful coverage of new code.

## 4. Commit messages

- Imperative subject, scoped, ≤ ~72 chars: `verifiers: add exact-match reward fn`.
- Explain *why* in the body when it isn't obvious.
- We use [Conventional Commits](https://www.conventionalcommits.org/) prefixes
  (`feat:`, `fix:`, `docs:`, `chore:`, `test:`, `refactor:`) so history and
  changelogs stay machine-readable.

## 5. Pull requests & merging

1. Open a PR against `main`. Fill in what changed and why.
2. **CI must be green** (ruff lint + format + pytest).
3. **At least one approving review** is required.
4. We **squash-merge** PRs — each PR becomes one clean commit on `main`.
5. Keep PRs small; large PRs are hard to review and slow to land.

> Maintainers: enable branch protection on `main` to enforce CI + review + squash.

## 6. Reporting issues

Open a [GitHub issue](https://github.com/camel-ai/camel-env/issues) with a clear
title, what you expected, what happened, and a minimal repro if possible.

## License

By contributing, you agree your contributions are licensed under the project's
[Apache 2.0 License](LICENSE).
