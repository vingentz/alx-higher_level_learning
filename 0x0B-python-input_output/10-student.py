#!/usr/bin/python3

"""Class Student"""


class Student:
    """Defines class Student"""
    def __init__(self, first_name, last_name, age):
        """initializes Student class attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves dictionary representation of Student instance"""
        if attrs is None:
            return self.__dict__
        else:
            k = {}
            for attr in attrs:
                if hasattr(self, attr):
                    k[attr] = getattr(self, attr)
        return k
