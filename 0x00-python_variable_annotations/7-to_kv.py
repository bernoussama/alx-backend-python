#!/usr/bin/env python3
"""
    Basic annotations - string and int/float to tuple
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return a tuple with a string and the square of a number"""
    return (k, float(v**2))
