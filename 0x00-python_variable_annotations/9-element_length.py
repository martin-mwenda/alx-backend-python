#!/usr/bin/env python3
"""This function takes a list of elements and returns a new list
where each element is paired with its length. The length is
calculated using the built-in len() function."""

from typing import List, Tuple, Any


def element_length(lst: List[Any]) -> List[Tuple[Any, int]]:
    """
    Returns a list of tuples containing elements and their lengths.

    Args:
    lst (List[Any]): The input list containing elements of any type.

    Returns:
    List[Tuple[Any, int]]: A list of tuples where each tuple contains
                            an element from the input list and its length.
    """
    return [(i, len(i)) for i in lst]
