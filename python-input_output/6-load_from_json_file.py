#!/usr/bin/python3
"""Definition of the function load_from_json_file"""
import json


def load_from_json_file(filename):
    """Loads a Python object from a JSON file."""
    with open(filename, "r") as file:
        return json.load(file)
