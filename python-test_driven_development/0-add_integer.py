def add_integer(a, b=98):
    """Return the integer addition of a and b.

    Float arguments are typecasted to ints before addition is performed.

    Raises:
        TypeError: If either of a or b is a non-integer and non-float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or float")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer or float")
    else:
        a = round(a)
        b = round(b)
    return a + b
