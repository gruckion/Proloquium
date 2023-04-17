"""A module that provides CSV input and output functionality."""

import pytest

from csv_processor import CSVProcessor


@pytest.fixture()
def csv_file(tmp_path):
    data = [
        {'name': 'John', 'age': 28},
        {'name': 'Jane', 'age': 32},
    ]
    file_path = tmp_path / "test.csv"
    with open(file_path, "w") as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)
    return file_path


def test_read_csv(csv_file):
    expected_data = [
        {'name': 'John', 'age': '28'},
        {'name': 'Jane', 'age': '32'},
    ]
    assert CSVProcessor.read_csv(csv_file) == expected_data


def test_write_csv_with_list(csv_file, tmp_path):
    data = [
        {'name': 'John', 'age': 28},
        {'name': 'Jane', 'age': 32},
    ]
    file_path = tmp_path / "output.csv"
    CSVProcessor.write_csv(file_path, data)

    with open(file_path, "r") as file:
        assert file.read() == "name,age\nJohn,28\nJane,32\n"


def test_write_csv_with_dict(csv_file, tmp_path):
    data = {'name': 'John', 'age': 28}
    file_path = tmp_path / "output.csv"
    CSVProcessor.write_csv(file_path, data)

    with open(file_path, "r") as file:
        assert file.read() == "name,age\nJohn,28\n"