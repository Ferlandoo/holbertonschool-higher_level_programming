#!/usr/bin/python3
"""Defines an object attribute lookup function."""


def inherits_from(obj, a_class):
    """Checks if an object is an instance of a class that inherited from
    the specified class, otherwise False"""
    return issubclass(type(obj), a_class) and type(obj) != a_class
