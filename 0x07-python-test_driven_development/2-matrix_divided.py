#!/usr/bin/python3
"""
    2-matrix_divided.py
    This function Devides two matrixes
    return new matrix
"""


def matrix_divided(matrix, div):
    """ Function that devides 2 matrixes
            return new matrix
    """
    if matrix is None:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if any((len(matrix[0]) != len(d)) for d in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    new_matrix = [None] * len(matrix)
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if not isinstance(matrix[i][j], (float, int)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = [[round(i / div, 2) for i in row] for row in matrix[:]]
    return new_matrix
