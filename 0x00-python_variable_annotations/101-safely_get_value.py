#!/usr/bin/env python3
"""
Define a type variable that can be any type
"""
from typing import Mapping, Any, Union, TypeVar, Optional


T = TypeVar('T')


def safely_get_value(dct: Mapping,
                     key: Any,
                     default: Optional[T] = None
                     ) -> Any | T:
    """
    Processes a list of elements and returns a new list of the same type.

    Args:
    data (List[T]): A list of elements of any type.

    Returns:
    List[T]: A new list containing processed elements of the same typ
    """
    if key in dct:
        return dct[key]
    else:
        return default
