#!/usr/bin/python3
class Rectangle(BaseGeometry):
    """This is A Class Called Rectangle"""
    def __init__(self, width, height):
        """Instance of the class with width and height"""
        BaseGeometry.integer_validator(self, "width", width)
        BaseGeometry.integer_validator(self, "height", height)
        self.__width = width
        self.__height = height
