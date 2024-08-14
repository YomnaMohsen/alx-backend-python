#!/usr/bin/env python3
"""mixed list module"""
from typing import List, Union


def sum_mixed_list(mylist: List[Union[int, float]]) -> float:
    """return sum of list"""
    return float(sum(mylist))
