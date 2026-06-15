# camel-env

[![CI](https://github.com/camel-ai/camel-env/actions/workflows/ci.yml/badge.svg)](https://github.com/camel-ai/camel-env/actions/workflows/ci.yml)
[![PyPI](https://img.shields.io/pypi/v/camel-env.svg)](https://pypi.org/project/camel-env/)
[![Python](https://img.shields.io/pypi/pyversions/camel-env.svg)](https://pypi.org/project/camel-env/)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

> **Environment-as-a-service** — a framework-agnostic layer that sits between
> training frameworks and datasets of environments.

`camel-env` models an **environment** as a triplet:

```
environment = (instruction, sandboxes, verification / reward_fn)
```

Everything is configurable via YAML and decoupled from any specific training
framework, so you can **train and evaluate agents through one unified interface**.

> ⚠️ **Status: early / alpha.** The API is taking shape and modules are being
> filled in. See the [roadmap](docs/roadmap.md) and [design](docs/design.md).

## Features

- 🧩 **Composable** — plug in your own agents, reward functions, and sandboxes.
- 📝 **Config-first** — wire everything from YAML; no hardcoded choices.
- 🔌 **Framework-agnostic** — decoupled from any training framework; the environment knows nothing about your trainer.
- 🚀 **Environment-as-service** — expose environments over a service boundary.

## Installation

`camel-env` uses [**uv**](https://docs.astral.sh/uv/) for fast, reproducible
environments. [Install uv](https://docs.astral.sh/uv/getting-started/installation/) first:

```bash
# macOS / Linux
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### As a user (install the package)

```bash
uv pip install camel-env          # into the active environment
# or, in your own uv project:
uv add camel-env
```

> Not yet published to PyPI. Until the first release, install from source — see below.

### From source (contributors & early adopters)

```bash
git clone https://github.com/camel-ai/camel-env.git
cd camel-env
uv sync                # creates .venv and installs the package + dev tools
uv run python -c "import camel_env; print(camel_env.__version__)"
```

That's it — `uv sync` reads [pyproject.toml](pyproject.toml), resolves
dependencies, creates a virtual environment in `.venv/`, and installs `camel-env`
in editable mode. No manual `venv`/`pip` steps needed.

## Quickstart

> 🚧 The public API is under construction. This section will show how to define
> an environment from YAML, run an agent in it, and compute a reward. Track
> progress in the [roadmap](docs/roadmap.md).

### Evaluation

_Coming soon._

### Train

_Coming soon._

## Documentation

- [Design](docs/design.md) — the core architecture and goals.
- [Roadmap](docs/roadmap.md) — what's planned and in what order.
- [Contributing](CONTRIBUTING.md) — dev setup, testing, and PR/merge rules.
- [`brain/`](brain/) — long-term project memory (decisions, conventions, glossary).

## Development

```bash
uv sync                              # set up the dev environment
uv run pytest                        # run the test suite
uv run ruff check . && uv run ruff format .   # lint + format
```

See [CONTRIBUTING.md](CONTRIBUTING.md) for the full workflow.

## License

Apache License 2.0 — see [LICENSE](LICENSE).
