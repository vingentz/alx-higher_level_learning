#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for k in range(len(matrix)):
        for l in range(len(matrix[k])):
            if l != 0:
                print(" ", end='')
            print("{:d}".format(matrix[k][l]), end='')
        print()
