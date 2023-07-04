#!/usr/bin/python3

"""add_integer adds 2 integers"""


def add_integer(a, b=98):
    """
    Calculates addition of a and b
    Args:
        a(int, float)
        b(int, float)
    """

    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")

    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)

    return a + b
