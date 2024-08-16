#!/usr/bin/env python3
"""duck type module"""
from typing import Tuple, Sequence, Iterable, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """function that returns list of tuples"""
    return [(i, len(i)) for i in lst]
