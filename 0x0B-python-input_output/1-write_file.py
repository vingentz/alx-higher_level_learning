#!/usr/bin/python3

"""String from textfile"""


def write_file(filename="", text=""):
    """Function to write string to a text file
    returns the number of characters written"""
    with open(filename, 'w') as file:
        return file.write(text)
