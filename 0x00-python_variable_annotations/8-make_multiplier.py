#!/usr/bin/env python3
"""Multiply a float by a multiplier"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Make multiplier function"""
    def func(flt: float) -> float:
        return multiplier * flt
    return func
