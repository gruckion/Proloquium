"""Unit tests for CSV Processor module."""

import pytest
from csv_processor import CSVProcessor


@pytest.fixture
def csv_processor(tmp_path):
    """Fixture to create CSVProcessor instance with input and output files."""
    input_file = tmp_path / "input.csv"
    output_file = tmp_path / "output.csv"
    input_data = [
        {"Name": "John", "Age": "25", "Gender": "Male"},
        {"Name": "Jane", "Age": "30", "Gender": "Female"},
    ]
    with open(input_file, mode="w", newline="") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=input_data[0].keys())
        writer.writeheader()
        writer.writerows(input_data)
    return CSVProcessor(str(input_file), str(output_file))


def test_read_csv(csv_processor):
    """Test read_csv method."""
    expected_output = [
        {"Name": "John", "Age": "25", "Gender": "Male"},
        {"Name": "Jane", "Age": "30", "Gender": "Female"},
    ]
    assert csv_processor.read_csv() == expected_output


def test_process_csv(csv_processor):
    """Test process_csv method."""
    input_data = [
        {"Name": "John", "Age": "25", "Gender": "Male"},
        {"Name": "Jane", "Age": "30", "Gender": "Female"},
    ]
    expected_output = input_data
    assert csv_processor.process_csv(input_data) == expected_output


def test_write_csv(csv_processor):
    """Test write_csv method."""
    input_data = [
        {"Name": "John", "Age": "25", "Gender": "Male"},
        {"Name": "Jane", "Age": "30", "Gender": "Female"},
    ]
    csv_processor.write_csv(input_data)
    expected_output = [
        {"Name": "John", "Age": "25", "Gender": "Male"},
        {"Name": "Jane", "Age": "30", "Gender": "Female"},
    ]
    with open(csv_processor.output_file, mode="r") as csv_file:
        reader = list(csv.DictReader(csv_file))
        assert reader == expected_output