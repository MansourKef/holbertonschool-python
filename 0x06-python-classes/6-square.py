#!/usr/bin/python3
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
            raise ValueError("ize must be >= 0")
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
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

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
                    print("#", end='')
                print()

    def my_print(self):
        """Function prints # Based on Size Value"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    if i == self.__position[0] and j == self.__position[1] and not self.__position[1] > 0:
                        print("_", end='')
                    else:
                        print("#", end='')
                print()

