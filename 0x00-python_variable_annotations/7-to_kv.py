#!/usr/bin/env python3
"""tuple module"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """return str and float in tuple"""
    return (k, (v * v))
