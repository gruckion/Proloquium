"""CSV Processor module."""

import csv
import sys
from typing import List


class CSVProcessor:
    """CSV Processor class with methods to read input CSV, process it, and generate an output CSV."""

    def __init__(self, input_file: str, output_file: str):
        """
        Initialize CSV Processor.

        Args:
            input_file (str): input CSV file path.
            output_file (str): output CSV file path.
        """
        self.input_file = input_file
        self.output_file = output_file

    def read_csv(self) -> List[dict]:
        """
        Read input CSV file.

        Returns:
            List[dict]: List of dictionaries representing CSV rows.
        """
        with open(self.input_file, mode="r") as csv_file:
            reader = csv.DictReader(csv_file)
            return [row for row in reader]

    def process_csv(self, data: List[dict]) -> List[dict]:
        """
        Process input CSV data.

        Args:
            data (List[dict]): List of dictionaries representing CSV rows.

        Returns:
            List[dict]: List of dictionaries representing processed CSV rows.
        """
        # Process data here
        return data

    def write_csv(self, data: List[dict]) -> None:
        """
        Write processed CSV data to output file.

        Args:
            data (List[dict]): List of dictionaries representing processed CSV rows.
        """
        with open(self.output_file, mode="w", newline="") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)


if __name__ == "__main__":
    processor = CSVProcessor(sys.argv[1], sys.argv[2])
    csv_data = processor.read_csv()
    processed_data = processor.process_csv(csv_data)
    processor.write_csv(processed_data)