#!/usr/bin/python3
"""Defines matrix multiplication using NumPy."""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiplication of two matrices.
    Args:
        m_a (list of lists of ints/floats): Matrix 1
        m_b (list of lists of ints/floats): Matrix 2
    """

    return (np.matmul(m_a, m_b))
