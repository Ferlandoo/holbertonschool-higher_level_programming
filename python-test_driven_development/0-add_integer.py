from typing import Union

def add_integer(a: Union[int, float], b: Union[int, float] = 98) -> int:
    """Return the integer addition of a and b.

    Float arguments are typecasted to ints before addition is performed.

    Raises:
        TypeError: If either of a or b is a non-integer and non-float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError('a must be an integer')
    if not isinstance(b, (int, float)):
        raise TypeError('b must be an integer')
    return int(a) + int(b)

if __name__ == '__main__':
    import doctest
    doctest.testfile('tests/0-add_integer.txt')
