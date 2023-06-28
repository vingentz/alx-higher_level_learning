#!/usr/bin/python3
'''Defines class Square with private attribute size'''


class Square:
    '''class sqaure definition with attribute size'''
    def __init__(self, size=0):
        '''initialize the size of a side of square'''
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
