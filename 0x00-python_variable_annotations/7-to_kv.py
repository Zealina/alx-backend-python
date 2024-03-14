#!/usr/bin/env python3
"""Create Tuple Annotations"""


def to_kv(k: str, v: int | float) -> tuple[str, float]:
    """Create a Tuple based on annotation"""
    return (k, float(v))
