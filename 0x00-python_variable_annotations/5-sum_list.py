#!/usr/bin/env python3
"""Define list of floats"""


def sum_list(input_list: list[float]) -> float:
    """Reduce the lsit by addition and return"""
    result: float = float(0)
    for a in input_list:
        result += a
    return result
