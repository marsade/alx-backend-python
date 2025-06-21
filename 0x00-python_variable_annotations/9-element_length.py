#!/usr/bin/env python3
'''Complex annotations - Iterable'''
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''Return a list of tuples with the length of each element in lst'''
    return [(i, len(i)) for i in lst]
