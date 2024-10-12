#!/usr/bin/env python3

"""This function takes a list of float numbers as input and
calculates their sum. It is useful for aggregating numeric
data in float format."""


def sum_list(input_list: List[float]) -> float:
    """
    Sums a list of floats and returns the total.

     Args:
    input_list (List[float]): The list of floats to be summed.

    Returns:
    float: The total sum of the input list.
    """
    return sum(input_list)
