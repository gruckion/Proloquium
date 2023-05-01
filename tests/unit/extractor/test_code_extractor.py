import pytest

from src.extractor.code_extractor import extract_file_name_and_code


@pytest.fixture
def input_text_single_file():
    return (
        "This is an example text with a file name and a code block.\n"
        "File: `project_name/src/example.py`\n"
        "```python\n"
        "def example_function():\n"
        '    return "Hello, world!"\n'
        "```\n"
    )


@pytest.fixture
def input_text_no_file_name():
    return (
        "This is an example text with no file name, only a code block.\n"
        "```python\n"
        "def example_function():\n"
        '    return "Hello, world!"\n'
        "```\n"
    )


@pytest.fixture
def input_text_no_code_block():
    return "This is an example text with a file name but no code block.\n" "File: `project_name/src/example.py`\n"


@pytest.fixture
def input_text_multiple_files():
    return (
        "This is an example text with multiple file names and code blocks.\n"
        "File: `project_name/src/example_1.py`\n"
        "```python\n"
        "def example_function1():\n"
        '    return "Hello, world!"\n'
        "```\n"
        "\n"
        "File: `project_name/src/example_2.py`\n"
        "```python\n"
        "def example_function2():\n"
        '    return "Goodbye, world!"\n'
        "```\n"
    )


def test_single_file(input_text_single_file):
    expected_output = [
        (
            "project_name/src/example.py",
            'def example_function():\n    return "Hello, world!"',
        )
    ]
    assert extract_file_name_and_code(input_text_single_file) == expected_output


def test_no_file_name(input_text_no_file_name):
    assert not extract_file_name_and_code(input_text_no_file_name)


def test_no_code_block(input_text_no_code_block):
    assert not extract_file_name_and_code(input_text_no_code_block)


def test_multiple_files(input_text_multiple_files):
    expected_output = [
        (
            "project_name/src/example_1.py",
            'def example_function1():\n    return "Hello, world!"',
        ),
        (
            "project_name/src/example_2.py",
            'def example_function2():\n    return "Goodbye, world!"',
        ),
    ]
    assert extract_file_name_and_code(input_text_multiple_files) == expected_output
