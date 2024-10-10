#!/usr/bin/env python3
"""
    Basic annotations - duck typing
"""
from typing import Iterable, List, Sequence, Tuple


def element_length(
        lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Return a list of tuples containing the element and its length
    """
    return [(i, len(i)) for i in lst]
