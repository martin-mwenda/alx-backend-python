#!/usr/bin/env python3
""" The floor function rounds down the input float to the nearest
integer less than or equal to the given number."""

import math


def floor(n: float) -> int:
    """
    Returns the floor of the given float.

    Args:
    n (float): The input float.

    Returns:
    float: The floor value of the input float.
    """
    return math.floor(n)
