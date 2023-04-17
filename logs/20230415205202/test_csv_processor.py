"""Unit tests for CSVProcessor"""

import csv
import io
from typing import List, Dict
import pytest
from csv_processor import CSVProcessor


@pytest.fixture(scope="module")
def input_csv_file():
    # Create an in-memory CSV file for testing purposes
    csv_data = io.StringIO()
    writer = csv.writer(csv_data)
    writer.writerow(["first_name", "last_name", "email"])
    writer.writerow(["John", "Doe", "JOHN.DOE@EXAMPLE.COM"])
    writer.writerow(["Jane", "Doe", "jane.doe@example.com"])
    csv_data.seek(0)
    return csv_data


@pytest.fixture(scope="module")
def expected_output_csv():
    # Create an in-memory CSV file for testing purposes
    csv_data = io.StringIO()
    writer = csv.writer(csv_data)
    writer.writerow(["first_name", "last_name", "email"])
    writer.writerow(["John", "Doe", "john.doe@example.com"])
    writer.writerow(["Jane", "Doe", "jane.doe@example.com"])
    csv_data.seek(0)
    return csv_data


def test_read_csv(input_csv_file):
    rows = CSVProcessor.read_csv(input_csv_file)
    assert isinstance(rows, list)
    assert len(rows) == 2
    assert isinstance(rows[0], dict)
    assert set(rows[0].keys()) == {"first_name", "last_name", "email"}
    assert rows[0]["first_name"] == "John"
    assert rows[0]["last_name"] == "Doe"
    assert rows[0]["email"] == "JOHN.DOE@EXAMPLE.COM"


def test_process_csv():
    rows = [
        {"first_name": "John", "last_name": "Doe", "email": "john.doe@example.com"},
        {"first_name": "Jane", "last_name": "Doe", "email": "jane.doe@example.com"},
    ]
    processed_rows = CSVProcessor.process_csv(rows)
    assert isinstance(processed_rows, list)
    assert len(processed_rows) == 2
    assert isinstance(processed_rows[0], dict)
    assert set(processed_rows[0].keys()) == {"first_name", "last_name", "email"}
    assert processed_rows[0]["first_name"] == "John"
    assert processed_rows[0]["last_name"] == "Doe"
    assert processed_rows[0]["email"] == "john.doe@example.com"


def test_write_csv(expected_output_csv):
    rows = [
        {"first_name": "John", "last_name": "Doe", "email": "john.doe@example.com"},
        {"first_name": "Jane", "last_name": "Doe", "email": "jane.doe@example.com"},
    ]
    output_csv_file = io.StringIO()
    CSVProcessor.write_csv(output_csv_file, rows)
    output_csv_file.seek(0)
    expected_output_csv.seek(0)
    assert output_csv_file.read() == expected_output_csv.read()
