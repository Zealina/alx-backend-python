#!/usr/bin/env python3
"""Type Annotations"""


from typing import TypeVar, Mapping, Union, Any


T = TypeVar('T')

def safely_get_value(
        dct: Mapping,
        key: Any,
        default: Union[T, None] = None) -> Union[Any, T]:
    """Create Type Safety"""
    if key in dct:
        return dct[key]
    else:
        return default
