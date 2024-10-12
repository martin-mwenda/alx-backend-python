#!/usr/bin/env python3
"""This function takes a list containing both integers and float
numbers as input and calculates their sum, returning the result
as a float."""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    return sum(mxd_lst)
