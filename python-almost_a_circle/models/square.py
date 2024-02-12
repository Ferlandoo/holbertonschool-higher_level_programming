#!/usr/bin/python3
'''Class Square inherits from Rectangle'''
from .rectangle import Rectangle


class Square(Rectangle):
    '''Class Square'''
    def __init__(self, size, x=0, y=0, id=None):
        '''Constructor'''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''String representation'''
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        '''Size of this square'''
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        '''Update the square's attributes'''
        if len(args) > 0:
            attributes = ["id", "size", "x", "y"]
            for i in range(len(args)):
                setattr(self, attributes[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        '''Return the dictionary representation of a square'''
        return {"id": self.id, "size": self.width, "x": self.x, "y": self.y}
