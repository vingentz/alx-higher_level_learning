#!/usr/bin/python3
"""1-my_list"""


class MyList(list):
    """list subclass"""
    def __init__(self):
        """initialize object"""
        super().__init__()

    def print_sorted(self):
        """print sorted list"""
        print(sorted(self))
