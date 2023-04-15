"""This module contains a function to read files."""

import os


def read_file_content(file_path: str) -> str:
    """Read the content of a file from the project root

    Args:
        file_path (str): The path of the file

    Returns:
        str: The content of the file
    """
    project_root = os.path.abspath(os.path.dirname(__file__))
    abs_file_path = os.path.join(project_root, file_path)

    try:
        with open(abs_file_path, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError as exception:
        print(f"Error: File '{file_path}' not found.")
        print(f"Working directory: {os.getcwd()}")
        print("Available files in the directory:")
        for file_name in os.listdir(project_root):
            print(file_name)

        raise FileNotFoundError(f"File '{file_path}' not found in project root.") from exception
