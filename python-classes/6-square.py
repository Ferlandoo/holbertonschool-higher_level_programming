#!/usr/bin/python3
"""Define a class Square."""


class Square:
    "Represent a square."""
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.position = position

    @property
    def size(self):
        """Get size of square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Initializes the data."""
        if type(value) is not int:
            print("size must be an integer", end="")
            raise TypeError
        if value < 0:
            print("size must be >= 0", end="")
            raise ValueError
        self.__size = value

    @property
    def position(self):
        """Get position of square"""
        return self.__position

    @position.setter
    def position(self, value):
        """Initializes the data."""
        if type(value) is not tuple:
            print("position must be a tuple of 2 positive integers", end="")
            raise TypeError
        if len(value) != 2:
            print("position must be a tuple of 2 positive integers", end="")
            raise TypeError
        if type(value[0]) is not int or type(value[1]) is not int:
            print("position must be a tuple of 2 positive integers", end="")
            raise TypeError
        if value[0] < 0 or value[1] < 0:
            print("position must be a tuple of 2 positive integers", end="")
            raise TypeError
        self.__position = value

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
