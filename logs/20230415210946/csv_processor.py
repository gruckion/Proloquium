"""This module contains a CSVProcessor class with methods to read input CSV, process it, and generate an output CSV."""

from typing import List, Dict
import csv


class CSVProcessor:
    """
    A class used to represent a CSV Processor

    ...

    Attributes
    ----------
    input_csv : str
        a string representing the path to the input CSV file
    output_csv : str
        a string representing the path to the output CSV file

    Methods
    -------
    read_input_csv() -> List[Dict[str, str]]:
        Reads the input CSV file and returns a List of Dictionaries
    process_csv(rows: List[Dict[str, str]]) -> List[Dict[str, str]]:
        Processes the input CSV data and returns a List of Dictionaries
    generate_output_csv(processed_data: List[Dict[str, str]]):
        Writes the processed data to the output CSV file
    """

    def __init__(self, input_csv: str, output_csv: str) -> None:
        """
        Parameters
        ----------
        input_csv : str
            a string representing the path to the input CSV file
        output_csv : str
            a string representing the path to the output CSV file
        """

        self.input_csv = input_csv
        self.output_csv = output_csv

    def read_input_csv(self) -> List[Dict[str, str]]:
        """Reads the input CSV file and returns a List of Dictionaries"""

        with open(self.input_csv, mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            return [row for row in csv_reader]

    @staticmethod
    def process_csv(rows: List[Dict[str, str]]) -> List[Dict[str, str]]:
        """Processes the input CSV data and returns a List of Dictionaries"""

        # TODO: Implement CSV processing logic
        return rows

    def generate_output_csv(self, processed_data: List[Dict[str, str]]) -> None:
        """Writes the processed data to the output CSV file"""

        fieldnames = processed_data[0].keys()

        with open(self.output_csv, mode='w', newline='') as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            csv_writer.writeheader()
            csv_writer.writerows(processed_data)