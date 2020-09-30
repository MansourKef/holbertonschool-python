#!/usr/bin/python3


class MyInt(int):
    """This is A Class Called MyInt"""

    def __init__(self, value):
        """
        initialization of the class
        """
        self.__value = value

    def __ne__(self, obj):
        """
        change behaviour of ne
        """
        if self.__value == obj:
            return True
        else:
            return False

    def __eq__(self, obj):
        """
        change behaviour of ne
        """
        if self.__value == obj:
            return False
        else:
            return True
