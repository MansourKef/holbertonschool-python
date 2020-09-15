#!/usr/bin/python3
"""
    5-square.py
    Module that defines a Square With Fctions
"""


class Square():
    """This is An Square Class Based On The
    Square Class"""
    def __init__(self, size=0):
        """This is init function of this Class
        that sets the Value of size"""
        self.size = size

    @property
    def size(self):
        """Gets The Value Of The __size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets The Value Of The __size Based On Some conditions"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("ize must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Function That Returns the square area of the Square"""
        return self.__size * self.__size

    def my_print(self):
        """Function prints # Based on Size Value"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
