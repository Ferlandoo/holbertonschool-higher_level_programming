#!/usr/bin/python3
'''Class Square inherits from Rectangle'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''Class Square'''
    def __init__(self, size, x=0, y=0, id=None):
        '''Constructor'''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''String representation'''
        return f"[{type(self).__name__}] ({self.id}) {self.x}/{self.y} - {self.width}"
