import subprocess
import sys


def run_pytest(folder_path: str) -> str:
    """Run pytest against the specified folder.

    Args:
        folder_path (str): The folder path to run pytest against

    Returns:
        str: The output of the pytest run
    """
    try:
        result = subprocess.run([sys.executable, "-m", "pytest", folder_path], check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as error:
        return error.output
