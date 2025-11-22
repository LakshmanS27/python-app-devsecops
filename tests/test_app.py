"""
test_math_tools.py

Unit tests for the arithmetic functions in math_tools.py.
"""

from app import multiply, divide
import pytest

def test_multiply():
    """Test the multiply() function."""
    assert multiply(2, 3) == 6
    assert multiply(-1, 5) == -5
    assert multiply(0, 10) == 0

def test_divide():
    """Test the divide() function."""
    assert divide(10, 2) == 5
    assert divide(-9, 3) == -3

    # floating-point division
    assert divide(7, 2) == 3.5

def test_divide_by_zero():
    """Test that division by zero raises an error."""
    with pytest.raises(ValueError):
        divide(10, 0)
