#!/usr/bin/python3
"""
    4-print_square.py
    Function that prints a square with the character #.
    return None
"""


def print_square(size):
    """ Function that prints a square with the character #.
        return None
    """
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size == 0:
        print()
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
