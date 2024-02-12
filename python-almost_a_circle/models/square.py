#!/usr/bin/python
'''Class Square inherits from Rectangle'''
from .rectangle import Rectangle


class Square(Rectangle):
    '''Class Square'''
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, new_size):
        self.width = new_size
        self.height = new_size

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"
