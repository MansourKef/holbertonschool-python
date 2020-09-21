#!/usr/bin/python3
"""
    1-rectangle.py
    Module that defines a Rectangle return {}
"""


class Rectangle:
    """This is A Class Called Rectangle"""
    def __init__(self, width=0, height=0):
        """Instance Of The Class That Sets The Values"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """Gets The Value Of The __width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets The Value Of The __width Based On Some conditions"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Gets The Value Of The __height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets The Value Of The __height Based On Some conditions"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
