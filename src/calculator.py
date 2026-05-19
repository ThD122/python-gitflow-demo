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