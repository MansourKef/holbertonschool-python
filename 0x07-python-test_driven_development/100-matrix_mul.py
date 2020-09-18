#!/usr/bin/python3
"""
Module to multiply 2 matrices
"""


def matrix_mul(m_a, m_b):
    """
    Function to multiply 2 matrices and return the result
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if any(not isinstance(el, list) for el in m_a):
        raise TypeError("m_a must be a list of lists")
    if any(not isinstance(el, list) for el in m_b):
        raise TypeError("m_b must be a list of lists")
    if len(m_a) == 0:
        raise TypeError("m_a must be a list of lists")
    if len(m_b) == 0:
        raise TypeError("m_b must be a list of lists")
    for i in range(len(m_a)):
        for j in range(len(m_a[0])):
            if not isinstance(m_a[i][j], (float, int)):
                raise TypeError("m_a should contain only integers or floats")
    for i in range(len(m_b)):
        for j in range(len(m_b[0])):
            if not isinstance(m_b[i][j], (float, int)):
                raise TypeError("m_b should contain only integers or floats")
    if any((len(m_a[0]) != len(d)) for d in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if any((len(m_b[0]) != len(d)) for d in m_b):
        raise TypeError("each row of m_b must be of the same size")
    result = [[sum(a*b for a, b in zip(m_a_row, m_b_col))
               for m_b_col in zip(*m_b)] for m_a_row in m_a]
    return result
