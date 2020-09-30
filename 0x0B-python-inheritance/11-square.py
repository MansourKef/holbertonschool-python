#!/usr/bin/python3


Rectangle = __import__("9-rectangle.py").Rectangle


class Square(Rectangle):
    """This is A Class Called Square"""

    def __init__(self, size):
        """Instance of the class with width and height"""
        Rectangle.__init__(self, size, size)
        self.__size = size

    def area(self):
        """Return the area"""
        return Rectangle.area(self)

    def __str__(self):
        """change the print fct output"""
        return Rectangle.__str__(self)
