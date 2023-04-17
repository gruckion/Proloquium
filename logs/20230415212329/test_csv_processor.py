"""This module contains unit tests for the CSVProcessor class."""

import csv
from typing import List, Tuple
from unittest.mock import mock_open, patch

import pytest
from csv_processor import CSVProcessor


@pytest.fixture
def input_csv_data() -> List[Tuple]:
    """Fixture to provide sample input CSV data."""
    return [
        ('Name', 'Age', 'City'),
        ('Alice', '25', 'New York'),
        ('Bob', '30', 'Los Angeles'),
        ('Charlie', '35', 'Chicago'),
        ('David', '40', 'Houston'),
    ]


def test_read_input_csv(input_csv_data, tmp_path):
    """Test CSVProcessor.read_input_csv method."""
    # Create a sample input CSV file
    file_path = tmp_path / 'input.csv'
    with open(file_path, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerows(input_csv_data)

    # Call the read_input_csv method and assert the output
    output_csv_data = CSVProcessor.read_input_csv(str(file_path))
    assert output_csv_data == input_csv_data


def test_process_csv(input_csv_data):
    """Test CSVProcessor.process_csv method."""
    # Create a sample process function
    def process_func(row):
        name, age, city = row
        return (name.upper(), int(age) + 1, city.lower())

    # Call the process_csv method and assert the output
    output_csv_data = CSVProcessor.process_csv(input_csv_data, process_func)
    expected_output = [
        ('NAME', 26, 'new york'),
        ('BOB', 31, 'los angeles'),
        ('CHARLIE', 36, 'chicago'),
        ('DAVID', 41, 'houston'),
    ]
    assert output_csv_data == expected_output


def test_generate_output_csv(input_csv_data, tmp_path):
    """Test CSVProcessor.generate_output_csv method."""
    # Create a sample output CSV file
    file_path = tmp_path / 'output.csv'

    # Call the generate_output_csv method and assert the output file contents
    with patch('builtins.open', mock_open()) as mock_file:
        CSVProcessor.generate_output_csv(str(file_path), input_csv_data)
        mock_file.assert_called_once_with(str(file_path), mode='w', newline='')
        mock_file().writerow.assert_has_calls(
            [call(row) for row in input_csv_data],
            any_order=True,
        )