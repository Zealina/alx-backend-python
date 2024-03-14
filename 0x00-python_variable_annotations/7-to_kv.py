#!/usr/bin/env python3
"""Create Tuple Annotations"""


from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Create a Tuple based on annotation"""
    return (k, float(v))
