#!/usr/bin/env python3
import math
from typing import Optional

def binary_search(l, x):
    return binary_search_inner(l, x, 0, len(l) - 1)

# take care for the awkward indexing (floor and idx_left are coupled in a surprising way)
def binary_search_inner(l, x, idx_left, idx_right):
    if idx_left == idx_right:
        if x == l[idx_left]:
            return idx_left
        else:
            return
    else:
        idx = math.floor((idx_left + idx_right) / 2)
        if x < l[idx]:
            return binary_search_inner(l, x, idx_left, idx-1)
        elif x > l[idx]:
            return binary_search_inner(l, x, idx+1, idx_right)
        else: # must be equal
            return idx



print(binary_search([0, 1, 2, 3, 4, 5, 6], 0))
