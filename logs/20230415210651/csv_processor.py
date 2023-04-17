"""This module contains a CSVProcessor class with methods to read input CSV, process it, and generate an output CSV."""

import csv
from typing import List, Tuple


class CSVProcessor:
    """A class to handle CSV processing tasks."""

    @staticmethod
    def read_input_csv(file_path: str) -> List[Tuple[str]]:
        """
        Read the input CSV file and return its contents as a list of tuples.
        
        Args:
            file_path (str): The path of the input CSV file.
        
        Returns:
            A list of tuples representing the contents of the input CSV file.
        """
        with open(file_path, "r") as file:
            reader = csv.reader(file)
            return [tuple(row) for row in reader]

    @staticmethod
    def process_csv(data: List[Tuple[str]]) -> List[Tuple[str]]:
        """
        Process the input CSV data and return the processed data as a list of tuples.
        
        Args:
            data (List[Tuple[str]]): The input CSV data as a list of tuples.
        
        Returns:
            A list of tuples representing the processed CSV data.
        """
        # Replace underscores with spaces
        processed_data = []
        for row in data:
            processed_data.append(tuple(value.replace("_", " ") for value in row))
        return processed_data

    @staticmethod
    def generate_output_csv(file_path: str, data: List[Tuple[str]]):
        """
        Generate an output CSV file with the processed data.
        
        Args:
            file_path (str): The path of the output CSV file to be generated.
            data (List[Tuple[str]]): The processed CSV data to be written to the output CSV file.
        """
        with open(file_path, "w") as file:
            writer = csv.writer(file)
            writer.writerows(data)