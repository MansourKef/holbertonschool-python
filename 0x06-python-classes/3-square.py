#!/usr/bin/python3
"""
    3-square.py
    Module that defines a Square with fct area
"""


class Square():
    """This is An Square Class Based On The
    Square Class"""
    def __init__(self, size=0):
        """This is init function of this Class
        that sets the Value of size following some conditions"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Function That Returns the square area of the Square"""
        return self.__size * self.__size
