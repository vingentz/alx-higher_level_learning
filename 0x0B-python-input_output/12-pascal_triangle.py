#!/usr/bin/python3

"""Pascal's Triangle"""


def pascal_triangle(n):
    """Returns empty list if n <= 0
    You can assume n will be always an integer
    """
    pastri = []
    if n <= 0:
        return pastri
    if n == 0:
        return [[1]]

    pastri = [[1]]
    for i in range(n-1):
        pastri.append([a+b for a, b in zip([0] + pastri[-1], pastri[-1] + [0])])
    return pastri
