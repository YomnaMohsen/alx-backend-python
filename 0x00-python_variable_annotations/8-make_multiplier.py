#!/usr/bin/env python3
"""complex types module"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    def mul(x):
        return multiplier * x
    return mul
