#!/usr/bin/python
'''Class Square inherits from Rectangle'''
from .rectangle import Rectangle


class Square(Rectangle):
    '''Class Square'''
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        '''Str format'''
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"
