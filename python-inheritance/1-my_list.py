#!/usr/bin/python3
"""Defines a class MyList that inherits from list."""


class MyList(list):
    def __init__(self):
        """Initializes the object."""
        super().__init__()
        
    def print_sorted(self):
        """Prints the list, but sorted."""
        print(sorted(self))
