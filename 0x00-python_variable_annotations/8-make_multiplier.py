#!/usr/bin/env python3
"""
    Basic annotations - functions
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Make a function that multiplies a number by a given multiplier
    """
    return lambda value: value * multiplier
