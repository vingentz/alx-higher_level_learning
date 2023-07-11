#!/usr/bin/python3

"""Read from file"""


def read_file(filename=""):
    """Reads text from file and print to stdout"""
    with open(filename) as file:
        filerd = file.read()
    print(filerd, end="")
