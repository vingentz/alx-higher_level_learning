#!/usr/bin/python3

"""Class to JSON"""


def class_to_json(obj):
    """
    Returns dictionary description with simple data structure
    for JSON serialization of object"""
    return obj.__dict__
