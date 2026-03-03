from __future__ import annotations

from importlib.resources import files


def get_theme_paths() -> dict[str, str]:
    """
    Returns absolute filesystem paths to the package's templates/static directories.
    Use these in Sphinx conf.py.
    """
    pkg = files("turtini_sphinx_theme")
    return {
        "templates": str(pkg.joinpath("_templates")),
        "static": str(pkg.joinpath("_static")),
    }
