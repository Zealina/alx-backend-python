#!/usr/bin/env python3
"""Sum a mixed list"""


def sum_mixed_list(mxd_lst: list[int | float]) -> float:
    """Reduce a list with integers and floats"""
    result: float = 0.0
    for a in mxd_lst:
        result += a
    return result
