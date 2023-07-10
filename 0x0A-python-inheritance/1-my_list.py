#!/usr/bin/python3
"""
    1-my_list
"""


class MyList(list):
    """Class inheriting from list object"""

    def print_sorted(self):
        """print sorted list"""
        print(sorted(self))
