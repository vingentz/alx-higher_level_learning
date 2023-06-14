#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix_new = []
    for numbers in matrix:
        matrix_new.append(list(map(lambda x: x**2, numbers)))
    return matrix_new
