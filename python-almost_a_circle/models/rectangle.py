#!/usr/bin/python3
'''Class Rectangle inherits from Base'''
from .base import Base


class Rectangle(Base):
    '''Class Rectangle'''
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, new_width):
        if not isinstance(new_width, int):
            raise TypeError(f"width must be an integer")
        elif new_width <= 0:
            raise ValueError(f"width must be > 0")
        self.__width = new_width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, new_height):
        if not isinstance(new_height, int):
            raise TypeError(f"height must be an integer")
        elif new_height <= 0:
            raise ValueError(f"height must be > 0")
        self.__height = new_height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, new_x):
        if not isinstance(new_x, int):
            raise TypeError(f"x must be an integer")
        elif new_x < 0:
            raise ValueError(f"x must be >= 0")
        self.__x = new_x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, new_y):
        if not isinstance(new_y, int):
            raise TypeError(f"y must be an integer")
        elif new_y < 0:
            raise ValueError(f"y must be >= 0")
        self.__y = new_y
