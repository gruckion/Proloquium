"""A module that defines unit tests for CSVProcessor class."""

from typing import List, Dict
import csv_processor


def test_read_csv():
    """Tests read_csv method of CSVProcessor class."""
    csv_path = "test_data/input.csv"
    csv_processor_obj = csv_processor.CSVProcessor()
    expected_output = [
        {"id": "1", "name": "John", "age": "30", "city": "New York"},
        {"id": "2", "name": "Jane", "age": "25", "city": "San Francisco"},
        {"id": "3", "name": "Bob", "age": "40", "city": "Seattle"},
    ]
    assert csv_processor_obj.read_csv(csv_path) == expected_output


def test_process_csv():
    """Tests process_csv method of CSVProcessor class."""
    input_csv = [
        {"id": "1", "name": "John", "age": "30", "city": "New York"},
        {"id": "2", "name": "Jane", "age": "25", "city": "San Francisco"},
        {"id": "3", "name": "Bob", "age": "40", "city": "Seattle"},
    ]
    csv_processor_obj = csv_processor.CSVProcessor()
    assert csv_processor_obj.process_csv(input_csv) == input_csv


def test_generate_output_csv():
    """Tests generate_output_csv method of CSVProcessor class."""
    output_csv = [
        {"id": "1", "name": "John", "age": "30", "city": "New York"},
        {"id": "2", "name": "Jane", "age": "25", "city": "San Francisco"},
        {"id": "3", "name": "Bob", "age": "40", "city": "Seattle"},
    ]
    csv_path = "test_data/output.csv"
    csv_processor_obj = csv_processor.CSVProcessor()
    csv_processor_obj.generate_output_csv(output_csv, csv_path)

    with open(csv_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        generated_output = [row for row in csv_reader]

    assert generated_output == output_csv


def test_csv_processor():
    """Tests CSVProcessor class."""
    input_csv = [
        {"id": "1", "name": "John", "age": "30", "city": "New York"},
        {"id": "2", "name": "Jane", "age": "25", "city": "San Francisco"},
        {"id": "3", "name": "Bob", "age": "40", "city": "Seattle"},
    ]
    expected_output = input_csv
    csv_path = "test_data/output.csv"

    csv_processor_obj = csv_processor.CSVProcessor()

    assert csv_processor_obj.read_csv("test_data/input.csv") == input_csv
    assert csv_processor_obj.process_csv(input_csv) == expected_output
    csv_processor_obj.generate_output_csv(expected_output, csv_path)

    with open(csv_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        generated_output = [row for row in csv_reader]

    assert generated_output == expected_output