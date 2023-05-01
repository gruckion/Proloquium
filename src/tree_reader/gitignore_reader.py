from __future__ import annotations

from pathlib import Path


def read_gitignore(path: str = ".") -> list[str]:
    """
    Read .gitignore and return a list of patterns to be ignored.

    :param path: The path of the folder containing the .gitignore file.
    :return: A list of patterns to be ignored.
    """
    with open(Path(path) / ".gitignore", encoding="utf-8") as file:
        return [line.strip() for line in file.readlines() if not line.startswith("#")]
