#!/usr/bin/python3
# 2-matrix_divided.py
"""Defines a matrix division function."""


def matrix_divided(matrix, div):
    """
<<<<<<< HEAD
    Divides all elements of a matrix by a given divisor.

    Args:
        matrix (list): A matrix represented as a
        list of lists of integers or floats.
        div (int or float): The divisor.
=======
    Divide all elements of a matrix.

    Args:
        matrix (list): A list of lists of ints or floats.
        div (int/float): The divisor.

    Raises:
        TypeError: If the matrix contains non-numbers.
        TypeError: If the matrix contains rows of different sizes.
        TypeError: If div is not an int or float.
        ZeroDivisionError: If div is 0.
>>>>>>> 5f43a7ea63205ad378c0142c7f062d88a0e46bc6

    Returns:
        list: A new matrix with all elements divided
        by div, rounded to 2 decimal places.

    Raises:
        TypeError: If matrix is not a matrix
        (list of lists) of integers/floats,
                   or if div is not a number.
        TypeError: If each row of the matrix does not
        have the same size.
        ZeroDivisionError: If div is equal to zero.
    """
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(ele, int) or isinstance(ele, float))
                    for ele in [num for row in matrix for num in row])):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(num / div, 2) for num in row] for row in matrix]
