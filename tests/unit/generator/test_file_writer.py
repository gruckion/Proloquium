# pylint: disable=unused-argument

from unittest.mock import MagicMock, mock_open, patch

import pytest

from src.generator.file_writer import FileWriter


@pytest.fixture
def mock_prolouqium_project_dir() -> MagicMock:
    """Mock the 'prolouqium_project_dir' function with a MagicMock.

    Returns:
        MagicMock: Replaces the 'prolouqium_project_dir' function.
    """
    with patch(
        "src.generator.file_writer.prolouqium_project_dir",
        return_value="fake_directory",
    ) as mock_project_dir:
        yield mock_project_dir


@pytest.fixture
def python_file() -> FileWriter:
    """Create a Python file with the content 'print("Hello, world!")'.

    Returns:
        FileWriter: A Python file with the content 'print("Hello, world!")'.
    """
    return FileWriter(filename="example.py", content='print("Hello, world!")\n')


@pytest.fixture
def mock_file_open() -> MagicMock:
    """Mock the built-in 'open' function with a MagicMock.

    Returns:
        MagicMock: Replaces the built-in 'open' function.
    """
    with patch("builtins.open", mock_open()) as mock_file:
        yield mock_file


def test_python_file_save(
    python_file: FileWriter,
    mock_file_open: MagicMock,
    mock_prolouqium_project_dir: MagicMock,
) -> None:
    # pylint: disable=unused-argument
    python_file.save()
    mock_file_open.assert_called_once_with(
        "fake_directory/example.py", "w", encoding="utf-8"
    )
    mock_file_open().write.assert_called_once_with('print("Hello, world!")\n')


def test_python_file_save_overwrite(
    python_file: FileWriter,
    mock_file_open: MagicMock,
    mock_prolouqium_project_dir: MagicMock,
) -> None:
    """Test that the file is overwritten if it already exists.

    Args:
        python_file (FileWriter): A Python file with the content
        mock_file_open (MagicMock): Replaces the built-in 'open' function.
    """
    # Save the file
    python_file.save()

    # Save the file again, overwriting the existing content
    python_file.save()

    # Assert that the file is opened with the correct arguments and content
    mock_file_open.assert_called_with(
        "fake_directory/example.py", "w", encoding="utf-8"
    )
    assert mock_file_open.call_count == 2
    mock_file_open().write.assert_called_with('print("Hello, world!")\n')
    assert mock_file_open().write.call_count == 2
