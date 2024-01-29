#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = [[element**2 for element in idx] for idx in matrix]
    return new_matrix
