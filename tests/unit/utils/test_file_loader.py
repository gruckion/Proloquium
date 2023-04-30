# tests/unit/utils/test_file_loader.py
import os

from src.utilities.file_loader import load_file_content


def test_load_file_content():
    test_file_path = os.path.join(os.path.dirname(__file__), "test_file.txt")

    with open(test_file_path, "w", encoding="utf-8") as test_file:
        test_file.write("This is a test file.")

    content = load_file_content(test_file_path)
    os.remove(test_file_path)

    assert content == "This is a test file."
