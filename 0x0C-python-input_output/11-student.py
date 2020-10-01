#!/usr/bin/python3
"""
Module 11
"""


class Student:
    """
    Class Student
    """

    def __init__(self, first_name, last_name, age):
        """ Class Student Init of the class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """that retrieves a dictionary representation
        of a Student instance
        """
        return self.__dict__
