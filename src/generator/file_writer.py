from __future__ import annotations

from dataclasses import dataclass
import os


@dataclass
class FileData:
    name: str
    content: str


def save_files(project_path: str, files: list[FileData]):
    print(f"Saving files to {project_path}")
    for file_name, content in files:
        file_writer = FileWriter(filename=file_name, content=content)
        file_writer.save(project_path)


@dataclass(frozen=True)
class FileWriter:
    """A class to write content to a file."""

    filename: str
    content: str

    def save(self, project_path: str) -> None:
        """Save the content to the file."""

        print(f"Saving: {self.filename}")

        full_path = os.path.join(project_path, self.filename)
        if self.filename:
            os.makedirs(os.path.dirname(full_path), exist_ok=True)

        print(f"Saving to: {full_path}")
        with open(full_path, "w", encoding="utf-8") as file:
            file.write(self.content)
