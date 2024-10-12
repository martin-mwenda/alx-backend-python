#!/usr/bin/env python3
"""
This function takes a list and returns the first element. If the
list is empty, it returns None. The type of the elements in the list
is not known
"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Returns the first element of a list if it exists, otherwise returns None
    Args:
    lst (List[T]): A list of elements of any type.

    Returns:
    Optional[T]: The first element of the list if it exists, otherwise None.
    """
    if lst:
        return lst[0]
    else:
        return None
