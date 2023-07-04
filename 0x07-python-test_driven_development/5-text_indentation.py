#!/usr/bin/python3

"""Prints text with 2 new lines after . ? and :"""


def text_indentation(text):
    """
    Args:
        text(string)
        no space at the beginning or end of each printed line
    """

    if type(text) is not str:
        raise TypeError("text must be a string")
    
    for delim in ".:?":
        text = (delim + "\n\n").join(
                [line.strip(" ") for line in text.split(delim)])

    print(f"{text}", end="")
