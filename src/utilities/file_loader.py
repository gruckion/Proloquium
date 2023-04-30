from typing import Optional


def load_file_content(file_path: str, encoding: Optional[str] = "utf-8") -> str:
    """
    Load the content of a file.

    Args:
        file_path (str): The path to the file.
        encoding (Optional[str]): The file encoding. Default is 'utf-8'.

    Returns:
        str: The content of the file.
    """
    with open(file_path, "r", encoding=encoding) as file:
        return file.read()
