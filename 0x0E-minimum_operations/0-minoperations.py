#!/usr/bin/python3
"""
0-minoperations.py
"""


def minOperations(n):
    """
    function that returns
    mini operation numbers
    """
    if type(n).__name__ != int.__name__:
        return 0
    elif n <= 0:
        return 0
    else:
        number = n
        div = 2
        min_oper = 0
        while number > 1:
            if number % div == 0:
                number /= div
                min_oper += div
            else:
                div += 1
        return min_oper
