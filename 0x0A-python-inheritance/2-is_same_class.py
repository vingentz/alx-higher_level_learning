#!/usr/bin/python3
"""
Checks if object is an instance of the class
"""


def is_same_class(obj, a_class):
    """Exact same object
    returns True if the object is exactly an instance
    of the specified class ; otherwise False
    """
    if type(obj) is a_class:
        return True
    return False
