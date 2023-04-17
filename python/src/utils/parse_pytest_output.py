# pytest_result_parser.py

import re

from pydantic import BaseModel


class PytestResult(BaseModel):
    """The result of a pytest run.

    Args:
        BaseModel (BaseModel): The base model
    """
    collected: int
    passed: int
    duration: float
    errors_duration: float


def parse_pytest_output(output: str):
    """Parse the output of a pytest run.

    Args:
        output (str): The output of a pytest run

    Returns:

    """
    pattern = re.compile(r"collected\s(\d+)(?:\sitems)?(?:.*\n)+(\d+)?\s?(?:passed)?(?:.*)in\s([\d.]+)s(?:.*\n)*(?:\d+\serror(?:.*)in\s([\d.]+)s)?")

    match = pattern.search(output)

    if match:
        collected, passed, duration, errors_duration = match.groups()
        return {
            "collected": int(collected),
            "passed": int(passed) if passed else None,
            "duration": float(duration),
            "errors_duration": float(errors_duration) if errors_duration else None
        }
    else:
        return None
