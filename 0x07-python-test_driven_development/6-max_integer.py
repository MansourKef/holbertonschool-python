#!/usr/bin/python3
"""Module to find the max integer in a list
"""


def max_integer(list=[]):
    """Function to find and return the max integer in a list of integers
        If the list is empty, the function returns None
    """
    if list is None:
        raise ValueError("List must contain at least one integer vaue")
    if len(list) == 0:
        return None
    if not all(isinstance(i, int) for i in list):
        raise ValueError("all numbers should be integers")
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return result
