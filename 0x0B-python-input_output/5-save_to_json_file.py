#!/usr/bin/python3

"""Write and convert to JSON string"""

import json

"""JSON module"""


def save_to_json_file(my_obj, filename):
    """Writes an Object to text file using JSON representation"""
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
