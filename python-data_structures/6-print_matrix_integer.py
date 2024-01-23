#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for idx in matrix:
        for elements in idx:
            print("{}".format(elements), end=" ")
        print()
