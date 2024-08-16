#!/usr/bin/env python3
"""complex types module"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """takes float as arg and return function that 
    multiples 2 floats"""
    def mul(x):
        """multipy 2 floats"""
        return multiplier * x
    return mul
