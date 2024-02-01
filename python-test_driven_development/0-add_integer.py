#!/usr/bin/python3
def add_integer(a, b=98):
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or float")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer or float")
    else:
        a = round(a)
        b = round(b)
    return a + b
