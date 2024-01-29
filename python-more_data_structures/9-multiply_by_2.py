#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = dict((key, value * 2) for key, value in a_dictionary.items())
    return new_dict


# Write a function that returns a new dictionary with all values multiplied by 2

# Prototype: def multiply_by_2(a_dictionary):
# You can assume that all values are only integers
# Returns a new dictionary
# You are not allowed to import any module
