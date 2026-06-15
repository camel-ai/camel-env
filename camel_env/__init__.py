"""camel-env: environment-as-a-service for training and evaluating agents.

An *environment* is a triplet ``(instruction, sandboxes, verification/reward_fn)``,
configured via YAML and served independently of any training framework or AI tool.
See ``docs/design.md`` and ``brain/architecture.md`` for the full design.
"""

__version__ = "0.0.1"

__all__ = ["__version__"]
