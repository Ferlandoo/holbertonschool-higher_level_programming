#!/usr/bin/python3
"""Define a class Square."""


class Square:
    "Represent a square."""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get size of square"""
        return self.__size

    @property
    def position(self):
        """Get position of square"""
        return self.__position

    @size.setter
    def size(self, value):
        """Initializes the data."""
        self.__size = value
        if type(value) is not int:
            print("size must be an integer", end="")
            raise TypeError
        if value < 0:
            print("size must be >= 0", end="")
            raise ValueError

    @position.setter
    def position(self, value):
        """Initializes the data."""
        self.__position = value
        for idx in value:
            if type(idx) is not int:
                print("position must be a tuple of 2 positive integers", end="")
                raise TypeError
            if idx < 0:
                print("position must be a tuple of 2 positive integers", end="")
                raise ValueError

    def area(self):
        """returns the current square area"""
        return self.__size * self.__size

    def my_print(self):
        """print # for the size of square"""
        for i in range(self.__size):
            for k in range(self.__position[0]):
                print(" ", end="")
            for j in range(self.__size):
                print("#", end="")
            print()
        if self.__size == 0:
            print("")
