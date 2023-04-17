"""Tests for parse_pytest_output function."""

import pytest
from pytest import FixtureRequest

from utils import parse_pytest_output
from utils.pydantic_builder import BuildablePydanticBase


class TestOutput(BuildablePydanticBase):
    """The expected result of a pytest run.

    Args:
        BaseModel (BuildablePydanticBase): A buildable pydantic base
    """
    collected: int
    passed: int
    duration: float
    errors_duration: float = None


@pytest.fixture(params=[
    (
        """
        ============================= test session starts ==============================
        ...
        collected 13 items
        ...
        logs/20230415213356/test_math_operations.py .............                [100%]
        ============================== 13 passed in 0.01s ==============================
        """,
        TestOutput(collected=13, passed=13, duration=0.01)
    ),
    (
        """
        ============================= test session starts ==============================
        ...
        collected 5 items
        ...
        logs/20230415213356/test_math_operations.py .....                          [100%]
        =============================== 5 passed in 0.02s ==============================
        """,
        TestOutput(collected=5, passed=5, duration=0.02)
    )
])
def successful_output(request: FixtureRequest):
    """ Successful pytest output

    Args:
        request (FixtureRequest): The request object

    Returns:
        tuple: The output and the expected result
    """
    return request.param


@pytest.fixture(params=[
    (
        """
        ============================= test session starts ==============================
        ...
        collected 0 items / 1 error
        ...
        =============================== 1 error in 0.05s ===============================
        """,
        {
            "collected": 0,
            "passed": None,
            "duration": 0.05,
            "errors_duration": None
        }
    ),
    (
        """
        ============================= test session starts ==============================
        ...
        collected 1 item / 1 error
        ...
        =============================== 1 error in 0.03s ===============================
        """,
        {
            "collected": 1,
            "passed": None,
            "duration": 0.03,
            "errors_duration": None
        }
    )
])
def failed_output(request: FixtureRequest):
    """ Failed pytest output

    Args:
        request (FixtureRequest): The request object

    Returns:
        tuple: The output and the expected result
    """
    return request.param


@pytest.fixture
def invalid_output():
    """ Invalid pytest output

    Returns:
        str: The invalid output
    """
    return "Invalid pytest output"


def test_successful_pytest_output(successful_output):
    output, expected_result = successful_output
    result = parse_pytest_output(output)

    assert result == expected_result


def test_failed_pytest_output(failed_output):
    output, expected_result = failed_output
    result = parse_pytest_output(output)

    assert result == expected_result


def test_invalid_pytest_output(invalid_output):
    result = parse_pytest_output(invalid_output)

    assert result is None
