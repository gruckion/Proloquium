import csv
from typing import List, Tuple


class CSVProcessor:
    """
    This class provides methods to read input CSV, process it, and generate an output CSV.
    """

    def __init__(self, input_file: str, output_file: str):
        """
        Initializes the CSVProcessor with input and output file paths.
        """
        self.input_file = input_file
        self.output_file = output_file

    def read_input_csv(self) -> List[Tuple[str]]:
        """
        Reads the input CSV file and returns a list of tuples representing each row.
        """
        with open(self.input_file, "r") as f:
            reader = csv.reader(f)
            return [tuple(row) for row in reader]

    def process_csv(self, data: List[Tuple[str]]) -> List[Tuple[str]]:
        """
        Processes the input data and returns a list of tuples representing each processed row.
        This method can be overridden by a subclass to provide custom processing logic.
        """
        return data

    def write_output_csv(self, data: List[Tuple[str]]):
        """
        Writes the processed data to the output CSV file.
        """
        with open(self.output_file, "w", newline="") as f:
            writer = csv.writer(f)
            for row in data:
                writer.writerow(row)
