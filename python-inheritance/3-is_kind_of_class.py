#!/usr/bin/python3
"""Defines a function that checks if an object is an instance of a class."""


def inherits_from(obj, a_class):
    """Returns True if the object is an instance of a class that inherited"""
    if isinstance(obj, a_class):
        return True
    return False
