from __future__ import annotations

import fnmatch
from pathlib import Path


def tree(root: str | Path, ignore_patterns: list[str]) -> dict[str, dict | None]:
    """
    Create a nested dictionary representing the folder structure.

    :param root: The root folder to start the tree from.
    :param ignore_patterns: A list of patterns to be ignored.
    :return: A nested dictionary representing the folder structure.
    """

    def is_not_ignored(path: Path) -> bool:
        return not any(
            fnmatch.fnmatch(str(path), pattern) for pattern in ignore_patterns
        )

    def generate_structure(path: Path) -> dict[str, dict | None]:
        if path.is_dir():
            return {
                subpath.name: generate_structure(subpath)
                for subpath in filter(is_not_ignored, path.iterdir())
            }

        return None

    return generate_structure(Path(root))
