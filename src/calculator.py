"""Simple calculator module."""


def add(a, b):
    """Return sum of two numbers."""
    return a + b


def subtract(a, b):
    """Return difference of two numbers (a - b)."""
    return a - b

def multiply(a: float, b: float) -> float:
    """
    Return the product of two numbers.

    Args:
        a: First number
        b: Second number

    Returns:
        Product of a and b
    """
    return a * b


def divide(a: float, b: float) -> float:
    """
    Return the division of two numbers (a / b).

    Args:
        a: Numerator
        b: Denominator

    Returns:
        Quotient of a divided by b

    Raises:
        ValueError: If denominator b is zero
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b