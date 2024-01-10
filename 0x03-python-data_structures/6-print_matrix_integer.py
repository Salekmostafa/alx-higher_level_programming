#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for colon in row:
            print("{:d}".format(colon), end=" " if col != row[-1] else "")
        print()
