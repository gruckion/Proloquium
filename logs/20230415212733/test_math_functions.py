"""This module contains unit tests for math functions"""

from typing import Union
import pytest

from math_functions import add, subtract, divide, multiply


@pytest.mark.parametrize("num1, num2, expected_output", [
    (1, 2, 3),
    (-1, 2, 1),
    (0, 0, 0),
    (1.5, 2.5, 4),
    (-1.5, 2.5, 1),
    (1, -2, -1),
    (-1, -2, -3),
    (1.5, -2.5, -1),
    (-1.5, -2.5, -4),
])
def test_add(num1: Union[int, float], num2: Union[int, float], expected_output: Union[int, float]) -> None:
    assert add(num1, num2) == expected_output


@pytest.mark.parametrize("num1, num2, expected_output", [
    (1, 2, -1),
    (-1, 2, -3),
    (0, 0, 0),
    (1.5, 2.5, -1),
    (-1.5, 2.5, -4),
    (1, -2, 3),
    (-1, -2, 1),
    (1.5, -2.5, 4),
    (-1.5, -2.5, 1),
])
def test_subtract(num1: Union[int, float], num2: Union[int, float], expected_output: Union[int, float]) -> None:
    assert subtract(num1, num2) == expected_output


@pytest.mark.parametrize("num1, num2, expected_output", [
    (1, 2, 0.5),
    (-1, 2, -0.5),
    (0, 1, 0),
    (1.5, 2.5, 0.6),
    (-1.5, 2.5, -0.6),
    (1, -2, -0.5),
    (-1, -2, 0.5),
    (1.5, -2.5, -0.6),
    (-1.5, -2.5, 0.6),
])
def test_divide(num1: Union[int, float], num2: Union[int, float], expected_output: Union[int, float]) -> None:
    assert divide(num1, num2) == expected_output

    
def test_divide_by_zero() -> None:
    with pytest.raises(ValueError):
        assert divide(2, 0)
        

@pytest.mark.parametrize("num1, num2, expected_output", [
    (1, 2, 2),
    (-1, 2, -2),
    (0, 0, 0),
    (1.5, 2.5, 3.75),
    (-1.5, 2.5, -3.75),
    (1, -2, -2),
    (-1, -2, 2),
    (1.5, -2.5, -3.75),
    (-1.5, -2.5, 3.75),
])
def test_multiply(num1: Union[int, float], num2: Union[int, float], expected_output: Union[int, float]) -> None:
    assert multiply(num1, num2) == expected_output