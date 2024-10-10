#!/usr/bin/env python3
"""
    Basic annotations - list of floats
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Return sum of mixed list"""
    return sum(mxd_lst)
