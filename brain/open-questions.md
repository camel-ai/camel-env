# Open Questions

Known unknowns, gotchas, and the backlog the brain should resolve. When you
answer one, move the conclusion into the right living doc (or
[decisions.md](decisions.md)) and delete it here.

## Backlog

- [x] ~~Packaging & tooling~~ — resolved: `uv` + `hatchling` + `ruff` + `pytest` (minimal).
  See [decisions.md](decisions.md), codified in [conventions.md](conventions.md).
- [x] ~~CI / GitHub workflows~~ — resolved: `.github/workflows/ci.yml` (py3.10–3.13).
- [x] ~~Unit tests~~ — smoke tests in `tests/`; real tests land with each feature.
- [ ] **Branch protection** — enable on `main` (require CI + 1 review + squash).
  This is a GitHub *repo setting* a maintainer must toggle; can't be done in-repo.
- [ ] **Optional future checks** — `pre-commit` hooks. Type checking and coverage
  are intentionally out for now; only revisit if the project clearly needs them.
- [ ] **Wider Python matrix** — CI currently tests 3.10 + 3.13 only; expand to the
  full 3.10–3.13(+) range before a public release if broad support is promised.
- [ ] **Pin dependency lower bounds** — deps are unpinned now; add bounds when a
  real incompatibility surfaces or before the first PyPI release.
- [ ] **PyPI publishing (CD)** — add a release workflow that publishes on tag.
  Needs a PyPI account + trusted-publisher / token setup.
- [ ] **Module implementations** — every `camel_env/*` package is still an empty
  shell (`__init__.py` only); intended responsibilities are in
  [architecture.md](architecture.md). Fill in per [roadmap](../docs/roadmap.md) M1.
- [ ] **Config schema** — the YAML format that wires environments, agents,
  sandboxes, and reward functions is not yet defined.
- [ ] **Examples & docs site** — `examples/` is empty; docs website (roadmap M3).
- [ ] **Core runtime deps** — only `pyyaml` is declared. Decide on config
  validation (e.g. `pydantic`) when the config schema is designed.

## Gotchas
<!-- Record non-obvious traps here as you hit them. -->

_(none yet)_
