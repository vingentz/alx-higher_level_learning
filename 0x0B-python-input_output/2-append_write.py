#!/usr/bin/python3

"""Append to file"""


def append_write(filename="", text=""):
    """Append string to end of text file
    returns number of xters added"""
    with open(filename, 'a') as file:
        return file.write(text)
