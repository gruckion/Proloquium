[test_csv_processor.py]
```python
"""This module contains pytest unit tests for the CSVProcessor class."""

from typing import List, Dict
import pytest
from csv_processor import CSVProcessor


@pytest.fixture
def input_csv_file(tmp_path):
    file_path = tmp_path / "input.csv"
    with open(file_path, "w", newline="") as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(["name", "age"])
        csv_writer.writerow(["Alice", "25"])
        csv_writer.writerow(["Bob", "30"])
    return file_path


@pytest.fixture
def output_csv_file(tmp_path):
    return tmp_path / "output.csv"


def test_read_csv(input_csv_file):
    expected_output = [{"name": "Alice", "age": "25"}, {"name": "Bob", "age": "30"}]
    assert CSVProcessor.read_csv(input_csv_file) == expected_output


def test_write_csv(output_csv_file):
    data = [{"name": "Alice", "age": "25"}, {"name": "Bob", "age": "30"}]
    fieldnames = ["name", "age"]
    CSVProcessor.write_csv(output_csv_file, data, fieldnames)
    with open(output_csv_file, "r") as file:
        csv_reader = csv.reader(file)
        assert next(csv_reader) == fieldnames
        assert next(csv_reader) == ["Alice", "25"]
        assert next(csv_reader) == ["Bob", "30"]
```