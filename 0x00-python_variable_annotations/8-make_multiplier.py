#!/usr/bin/env python3
"""This function takes a float as input and returns a new function tha
can multiply any float by the provided multiplier. The returned function
can be called with a float argument to get the product."""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by a given multiplier.

    This function takes a float as input and returns a new function that
    can multiply any float by the provided multiplier. The returned function
    can be called with a float argument to get the product.

    Args:
    multiplier (float): The multiplier to use for multiplication.

    Returns:
    Callable[[float], float]: A function that takes a float returns it product
                               with the multiplier.
    """
    def multiply(value: float) -> float:
        """Multiplies the given value by the multiplier."""
        return value * multiplier

    return multiply
