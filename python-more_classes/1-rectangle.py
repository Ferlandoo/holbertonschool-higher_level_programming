#!/usr/bin/python3
"""Module that defines a rectangle"""


class Rectangle:
    """Class that defines a rectangle"""
    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    @property
    def width(self):
        '''Return width.'''
        return self.__width

    @width.setter
    def width(self, value):
        '''Change width.'''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''Return height.'''
        return self.__height

    @height.setter
    def height(self, value):
        '''Change height.'''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__height = value
