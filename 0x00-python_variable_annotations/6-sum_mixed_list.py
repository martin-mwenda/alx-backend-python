#!/usr/bin/env python3
"""This function takes a list containing both integers and float
numbers as input and calculates their sum, returning the result
as a float."""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Sums a list of integers and floats and returns the total.
    return sum(mxd_lst)

     Args:
    mxd_lst (List[Union[int, float]]): The list of integers and floats summed

    Returns:
    float: The total sum of the input list.
    """
    return float(sum(mxd_lst))
