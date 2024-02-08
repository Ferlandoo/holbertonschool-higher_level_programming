#!/usr/bin/python3
"""Definition of the function save_to_json_file"""
import json


def save_to_json_file(my_obj, filename):
    """Saves a Python object to a JSON file."""
    with open(filename, "w") as file:
        return file.write(json.dumps(my_obj))
