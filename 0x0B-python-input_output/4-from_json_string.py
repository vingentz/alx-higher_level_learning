#!/usr/bin/python3

"""convert from JSON string to python data structure"""

import json

"""JSON module"""


def from_json_string(my_str):
    """Return a Python data structure represented with JSON string"""
    return json.loads(my_str)
