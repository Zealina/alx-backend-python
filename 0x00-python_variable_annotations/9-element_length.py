#!/usr/bin/env python3
"""Duck type function"""


from typing import Sequence, Iterable, List


def element_length(lst: Iterable[Sequence]) -> List[tuple[Sequence, int]]:
    """Return the length og the list"""
    return [(i, len(i)) for i in lst]
