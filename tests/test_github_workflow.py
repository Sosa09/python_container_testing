# tests/test_math_operations.py
import pytest
from math_operations import add, subtract, multiply, divide

def test_add():
    assert add(3, 2) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_subtract():
    assert subtract(3, 2) == 1
    assert subtract(2, 3) == -1
    assert subtract(5, 5) == 0

def test_multiply():
    assert multiply(3, 2) == 6
    assert multiply(0, 5) == 0
    assert multiply(-2, 3) == -6

def test_divide():
    assert divide(6, 2) == 3
    assert divide(5, 2) == 2.5

    # Testing for division by zero exception
    with pytest.raises(ValueError, match="Cannot divide by zero!"):
        divide(10, 0)
