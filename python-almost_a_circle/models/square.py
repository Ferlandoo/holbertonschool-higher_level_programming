#!/usr/bin/python
'''Class Square inherits from Rectangle'''
from .rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        '''Constructor'''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''String representation'''
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
