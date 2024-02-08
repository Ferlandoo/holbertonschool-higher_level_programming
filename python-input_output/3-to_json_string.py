#!/usr/bin/python3
"""Defines a function to convert Python objects to JSON strings."""


def to_json_string(my_obj):
    """Returns the JSON representation of an object (string)"""
    return my_obj.__str__()
