#!/usr/bin/env python3
"""Define list of floats"""


from typing import List


def sum_list(input_list: List[float]) -> float:
    """Reduce the lsit by addition and return"""
    result: float = 0.0
    for a in input_list:
        result += a
    return result
