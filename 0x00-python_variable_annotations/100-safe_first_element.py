#!/usr/bin/env python3
"""Properly Annotate External code"""


from typing import Sequence, Union, Any


# The types of the elements of the input are not known
def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Return the first element of an Sequence"""
    if lst:
        return lst[0]
    else:
        return None
