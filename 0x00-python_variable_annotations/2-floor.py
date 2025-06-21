#!/usr/bin/env python3
''' Basic annotation example - floor'''


def floor(n: float) -> int:
    """Returns the floor of a float."""
    return int(n) if n >= 0 else int(n) - 1
