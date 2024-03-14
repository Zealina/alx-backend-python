#!/usr/bin/env python3
"""Create Tuple Annotations"""


from typing import Tuple


def to_kv(k: str, v: int | float) -> Tuple[str, float]:
    """Create a Tuple based on annotation"""
    return (k, float(v))
