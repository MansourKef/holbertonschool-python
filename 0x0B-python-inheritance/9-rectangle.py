#!/usr/bin/python3
"""Module 9-rectangle.py"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """This is A Class Called Rectangle"""
    def __init__(self, width, height):
        """Instance of the class with width and height"""
        BaseGeometry.integer_validator(self, "width", width)
        BaseGeometry.integer_validator(self, "height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Return the area"""
        return self.__width * self.__height

    def __str__(self):
        """change the print fct output"""
        return "[{}] {}/{}".format(type(self).__name__,
                                   self.__width, self.__height)
