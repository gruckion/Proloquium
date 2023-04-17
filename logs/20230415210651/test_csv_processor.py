"""This module contains unit tests for the CSVProcessor class."""

from typing import List, Tuple
from csv_processor import CSVProcessor


def test_read_input_csv(tmp_path):
    """Test the read_input_csv method of the CSVProcessor class."""
    # Create a test CSV file
    test_file = tmp_path / "test.csv"
    with open(test_file, "w") as file:
        file.write("1,2,3\n4,5,6\n")
    # Call the method being tested
    result = CSVProcessor.read_input_csv(test_file)
    # Check the result
    expected = [("1", "2", "3"), ("4", "5", "6")]
    assert result == expected


def test_process_csv():
    """Test the process_csv method of the CSVProcessor class."""
    # Define test data
    data = [("1", "2", "3"), ("4", "5", "6")]
    # Call the method being tested
    result = CSVProcessor.process_csv(data)
    # Check the result
    expected = [("1", "2", "3"), ("4", "5", "6")]
    assert result == expected


def test_generate_output_csv(tmp_path):
    """Test the generate_output_csv method of the CSVProcessor class."""
    # Define test data
    data = [("1", "2", "3"), ("4", "5", "6")]
    # Create a test output file path
    test_file = tmp_path / "test.csv"
    # Call the method being tested
    CSVProcessor.generate_output_csv(test_file, data)
    # Read the output file and check its contents
    with open(test_file, "r") as file:
        reader = csv.reader(file)
        result = [tuple(row) for row in reader]
    expected = [("1", "2", "3"), ("4", "5", "6")]
    assert result == expected