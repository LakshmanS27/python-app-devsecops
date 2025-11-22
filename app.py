"""
math_tools.py

A simple Python module that provides basic arithmetic functions:
- multiply(a, b)
- divide(a, b)
"""

def multiply(a, b):
    """Return the product of two numbers."""
    return a * b

def divide(a, b):
    """Return the quotient of two numbers. Raises an error if division by zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

if __name__ == "__main__":
    print("Multiply 5 * 3 =", multiply(5, 3))
    print("Divide 10 / 2 =", divide(10, 2))
