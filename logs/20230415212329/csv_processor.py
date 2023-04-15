"""This module contains a CSVProcessor class with methods to read input CSV, process it, and generate an output CSV."""

import csv
from typing import Any, List, Tuple


class CSVProcessor:
    """CSVProcessor class with methods to read input CSV, process it, and generate an output CSV."""

    @staticmethod
    def read_input_csv(file_path: str) -> List[Tuple]:
        """
        Read input CSV file and returns its data as list of tuples.
        
        :param file_path: Path of the input CSV file.
        :return: List of tuples containing CSV data.
        """
        csv_data = []
        with open(file_path, mode='r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                csv_data.append(tuple(row))
        return csv_data

    @staticmethod
    def process_csv(csv_data: List[Tuple], process_func: Any) -> List[Tuple]:
        """
        Process input CSV data using the provided process function.
        
        :param csv_data: List of tuples containing CSV data.
        :param process_func: Function to process the CSV data.
        :return: List of tuples containing processed CSV data.
        """
        processed_data = []
        for row in csv_data:
            processed_row = process_func(row)
            processed_data.append(processed_row)
        return processed_data

    @staticmethod
    def generate_output_csv(file_path: str, csv_data: List[Tuple]) -> None:
        """
        Generate output CSV file using the provided CSV data.
        
        :param file_path: Path of the output CSV file.
        :param csv_data: List of tuples containing CSV data.
        """
        with open(file_path, mode='w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerows(csv_data)