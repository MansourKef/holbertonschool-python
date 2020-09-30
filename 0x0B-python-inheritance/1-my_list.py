#!/usr/bin/python3
"""
Module 1-my_list.py
"""


class MyList(list):
    """CLass Mylist Inherits from List"""

    def print_sorted(self):
        """Prints Sorted List"""
        print(sorted(self))
