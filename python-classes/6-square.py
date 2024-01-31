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

    @size.setter
    def size(self, value):
        """Initializes the data."""
        if type(value) is not int:
            raise TypeError("size must be an integer", end="")
        if value < 0:
            raise ValueError("size must be >= 0", end="")
        self.__size = value

    @property
    def position(self):
        """Get position of square"""
        return self.__position

    @position.setter
    def position(self, value):
        """Initializes the data."""
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not all(isinstance(i, int) and i >= 0 for i in value):
            raise ValueError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """returns the current square area"""
        return self.__size * self.__size

    def my_print(self):
        """print # for the size of square"""
        if self.__size == 0:
            print("")
        for i in range(self.__size):
            for k in range(self.__position[0]):
                print(" ", end="")
            for j in range(self.__size):
                print("#", end="")
            print()
