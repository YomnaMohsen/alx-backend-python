#!/usr/bin/env python3
"""sum list module"""


def sum_list(l: list[float]) -> float:
    sum = 0
    for item in l:
        sum += item
    return sum
