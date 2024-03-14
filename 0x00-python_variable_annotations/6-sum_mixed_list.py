#!/usr/bin/env python3
"""Sum a mixed list"""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Reduce a list with integers and floats"""
    result: float = 0.0
    for a in mxd_lst:
        result += a
    return result
