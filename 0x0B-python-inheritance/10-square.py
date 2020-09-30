#!/usr/bin/python3
"""Module 10-square.py"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """This is A Class Called Square"""

    def __init__(self, size):
        """Instance of the class with width and height"""
        super().__init__(size, size)
        self.__size = size
        Rectangle.integer_validator(self, "size", self.__size)

    def area(self):
        """Return the area"""
        return self.__size * self.__size
