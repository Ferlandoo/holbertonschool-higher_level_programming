def add_integer(a, b=98):
    """
    Adds two numbers and returns the result.

    Parameters:
    - a (int or float): The first number.
    - b (int or float, optional): The second number. Defaults to 98 if not provided.

    Returns:
    int: The sum of the two numbers after rounding them to the nearest integer.

    Raises:
    TypeError: If either 'a' or 'b' is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or float")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer or float")
    else:
        a = round(a)
        b = round(b)
    return a + b
