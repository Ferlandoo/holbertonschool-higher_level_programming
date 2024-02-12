#!/usr/bin/python3
'''Base class'''


class Base:
    '''Base class'''
    __nb_objects = 0
    def __init__(self, id=None):
        if id is not None:
            self.no_id = id
        Base.__nb_objects += 1        
