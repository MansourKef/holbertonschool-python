#!/usr/bin/python3
"""
Module to multiply 2 matrices
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Function to multiply 2 matrices and return the result
    using numpy
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_a must be a list")
    if any(not isinstance(el, list) for el in m_a):
        raise TypeError("m_a must be a list of lists")
    if any(not isinstance(el, list) for el in m_b):
        raise TypeError("m_b must be a list of lists")
    if len(m_a) == 0:
        raise TypeError("m_a must be a list of lists")
    if len(m_b) == 0:
        raise TypeError("m_b must be a list of lists")
    if not all([[isinstance(x, (float, int)) for x in sl] for sl in m_a]):
        raise TypeError("m_a should contain only integers or floats")
    if not all([[isinstance(x, (float, int)) for x in sl] for sl in m_b]):
        raise TypeError("m_b should contain only integers or floats")
    if any((len(m_a[0]) != len(d)) for d in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if any((len(m_b[0]) != len(d)) for d in m_b):
        raise TypeError("each row of m_b must be of the same size")
    result = np.dot(m_a, m_b)
    return result
