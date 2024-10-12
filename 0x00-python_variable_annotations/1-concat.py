#!/usr/bin/env python3
"""This function takes two input strings and combines them into a single
string It is useful for joining text data, such as first and last names, or
for creating longer messages from smaller segments."""


def concat(str1: str, str2: str) -> str:
    """
    Concatenates two strings and returns the result.

    Args:
    str1 (str): The first string.
    str2 (str): The second string.

    Returns:
    str: The concatenated result of str1 and str2.
    """
    return str1 + str2
