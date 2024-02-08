#!/usr/bin/python3
import json
"""Definition of the function load_from_json_file"""


def load_from_json_file(filename):
    """Loads a Python object from a JSON file."""
    with open(filename, encoding="utf-8") as file:
        return json.load(file)
