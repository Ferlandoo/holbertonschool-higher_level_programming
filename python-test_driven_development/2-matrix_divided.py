#!/usr/bin/python3
def matrix_divided(matrix, div):
    if not all(isinstance(row, list) for row in matrix) or \
     not all(isinstance(element, (int, float)) for row in matrix for element in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if any(len(row) != len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    result_matrix = []
    for row in matrix:
        new_row = []
        for element in row:
            new_row.append(round(element / div, 2))
        result_matrix.append(new_row)
    return result_matrix
