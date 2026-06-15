"""Smoke tests: the package imports and exposes a version.

These exist so CI has something real to run from day one. Replace/extend as
actual functionality lands — every new feature should ship with its own tests
(see brain/conventions.md).
"""

import camel_env


def test_package_imports() -> None:
    assert camel_env is not None


def test_has_version() -> None:
    assert isinstance(camel_env.__version__, str)
    assert camel_env.__version__
