#!/usr/bin/python3
"""
    Module that defines a BaseGeometry return {}
"""


class BaseGeometry:
    """This is An Empty Class Called BaseGeometry"""
    def area(self):
        """Return Area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
