#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    a_matrix = matrix.copy()

    for i in range(len(matrix)):
        a_matrix[i] = [x**2 for x in matrix[i]]

    return (a_matrix)
