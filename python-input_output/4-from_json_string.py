#!/usr/bin/python3
"""Definition of the function from_json_string"""
import json


def from_json_string(my_str):
    """Converts a JSON formatted string into a Python object."""
    return json.loads(my_str)
