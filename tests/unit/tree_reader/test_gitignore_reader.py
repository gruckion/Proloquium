from unittest.mock import mock_open, patch

import pytest

from src.tree_reader.gitignore_reader import read_gitignore


@pytest.fixture
def mock_gitignore_file():
    content = "# This is a comment\n*.pyc\n__pycache__\n"
    return mock_open(read_data=content)


def test_read_gitignore(mock_gitignore_file):
    expected_result = ["*.pyc", "__pycache__"]

    with patch("builtins.open", mock_gitignore_file, create=True):
        result = read_gitignore()
        assert result == expected_result
