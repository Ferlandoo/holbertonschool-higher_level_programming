#!/usr/bin/python3
"""Define a class Square."""


class Square:
    "Represent a square."""
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """Get size of square"""
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value
        """Initializes the data."""
        if type(value) is not int:
            print("size must be an integer", end="")
            raise TypeError
        if value < 0:
            print("size must be >= 0", end="")
            raise ValueError

    def area(self):
        """returns the current square area"""
        return self.__size * self.__size

    def my_print(self):
        """print # for the size of square"""
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()
        if self.__size == 0:
            print("")
