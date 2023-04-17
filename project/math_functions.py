"""
This module contains functions for performing basic mathematical operations.
"""

from typing import Union


def add(x: Union[int, float], y: Union[int, float]) -> Union[int, float]:
    """
    Returns the sum of two numbers x and y.

    Args:
    x (Union[int, float]): A number (int or float).
    y (Union[int, float]): A number (int or float).

    Returns:
    Union[int, float]: The sum of x and y.
    """
    return x + y


def subtract(x: Union[int, float], y: Union[int, float]) -> Union[int, float]:
    """
    Returns the difference of two numbers x and y.

    Args:
    x (Union[int, float]): A number (int or float).
    y (Union[int, float]): A number (int or float).

    Returns:
    Union[int, float]: The difference of x and y.
    """
    return x - y


def multiply(x: Union[int, float], y: Union[int, float]) -> Union[int, float]:
    """
    Returns the product of two numbers x and y.

    Args:
    x (Union[int, float]): A number (int or float).
    y (Union[int, float]): A number (int or float).

    Returns:
    Union[int, float]: The product of x and y.
    """
    return x * y


def divide(x: Union[int, float], y: Union[int, float]) -> Union[int, float]:
    """
    Returns the quotient of two numbers x and y.

    Args:
    x (Union[int, float]): A number (int or float).
    y (Union[int, float]): A number (int or float).

    Returns:
    Union[int, float]: The quotient of x and y.
    """
    if y == 0:
        raise ZeroDivisionError("division by zero is undefined")
    return x / y