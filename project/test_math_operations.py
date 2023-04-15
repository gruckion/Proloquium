[test_math_operations.py]
```python
"""Unit tests for math_operations.py"""

import pytest
from math_operations import add_numbers, subtract_numbers, multiply_numbers, divide_numbers

# add_numbers tests
def test_add_numbers_positive():
    assert add_numbers(2, 3) == 5

def test_add_numbers_negative():
    assert add_numbers(-2, -3) == -5

def test_add_numbers_mixed():
    assert add_numbers(-2, 3) == 1

# subtract_numbers tests
def test_subtract_numbers_positive():
    assert subtract_numbers(5, 3) == 2

def test_subtract_numbers_negative():
    assert subtract_numbers(-5, -3) == -2

def test_subtract_numbers_mixed():
    assert subtract_numbers(-2, 3) == -5

# multiply_numbers tests
def test_multiply_numbers_positive():
    assert multiply_numbers(2, 3) == 6

def test_multiply_numbers_negative():
    assert multiply_numbers(-2, -3) == 6

def test_multiply_numbers_mixed():
    assert multiply_numbers(-2, 3) == -6

# divide_numbers tests
def test_divide_numbers_positive():
    assert divide_numbers(6, 3) == 2

def test_divide_numbers_negative():
    assert divide_numbers(-6, -3) == 2

def test_divide_numbers_mixed():
    assert divide_numbers(-6, 3) == -2

def test_divide_numbers_zero_divisor():
    with pytest.raises(ZeroDivisionError):
        divide_numbers(6, 0)
```