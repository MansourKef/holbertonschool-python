#!/usr/bin/python3
"""
    101-square.py
    Module that defines a Square With Fctions
"""


class Square():
    """This is An Square Class Based On The
    Square Class"""
    def __init__(self, size=0, position=(0, 0)):
        """This is init function of this Class
        that sets the Value of size"""
        self.size = size
        self.position = position

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
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """Gets The Value Of The __position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets The Value Of The __position Based On Some conditions"""
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif any(type(v) != int for v in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif any(v < 0 for v in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Function That Returns the square area of the Square"""
        return self.__size * self.__size

    def my_print(self):
        """ Function that prints the area based on the size and position
        """
        if self.__size != 0:
            for k in range(self.__position[1]):
                print()

            for i in range(self.__size):
                for l in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print()
        else:
            print()

    def __str__(self):
        """Redefining Print Function"""
        s = ""
        if self.__size != 0:
            for k in range(self.__position[1]):
                s += "\n"

            for i in range(self.__size):
                for l in range(self.__position[0]):
                    s += " "
                for j in range(self.__size):
                    s += "#"
                s += "\n"
        else:
            s += "\n"
        return s[:-1]
