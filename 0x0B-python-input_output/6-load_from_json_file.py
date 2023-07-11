#!/usr/bin/python3

"""Create object from JSON file"""

import json
"""JSON module"""


def load_from_json_file(filename):
    """Function that creates an Object from JSON file"""
    with open(filename) as file:
        return json.load(file)
