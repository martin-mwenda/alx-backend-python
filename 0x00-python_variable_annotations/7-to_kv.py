#!/usr/bin/env python3

"""This function takes a string and a number (int or float) as inputs,
and returns a tuple where the first element is the string and the
second element is the square of the number, represented as a float."""

from typing import Union, Tuple

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Creates a tuple from a string and the square of a number.

    Args:
    k (str): The input string.
    v (Union[int, float]): The input number (int or float).

    Returns:
    Tuple[str, float]: A tuple containing the string and the square of the number.
    """
    return (k, float(v ** 2))
