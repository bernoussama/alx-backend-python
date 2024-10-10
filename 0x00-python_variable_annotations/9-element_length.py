#!/usr/bin/env python3
"""
    Basic annotations - functions
"""
from typing import List, Sequence, Tuple


def element_length(lst: Sequence) -> List[Tuple[Sequence, int]]:
    return [(i, len(i)) for i in lst]
