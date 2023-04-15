"""This module contains math functions for add, subtract, divide and multiply"""

from typing import Union


def add(num1: Union[int, float], num2: Union[int, float]) -> Union[int, float]:
    """Returns the sum of two numbers"""
    return num1 + num2


def subtract(num1: Union[int, float], num2: Union[int, float]) -> Union[int, float]:
    """Returns the difference between two numbers"""
    return num1 - num2


def divide(num1: Union[int, float], num2: Union[int, float]) -> Union[int, float]:
    """Returns the quotient of two numbers"""
    if num2 == 0:
        raise ValueError("Cannot divide by zero")
    return num1 / num2


def multiply(num1: Union[int, float], num2: Union[int, float]) -> Union[int, float]:
    """Returns the product of two numbers"""
    return num1 * num2