#!/usr/bin/python3
"""
Module that contains a function that multiplies two matrices using NumPy.
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using NumPy.

    Args:
        m_a (list of lists): The first matrix.
        m_b (list of lists): The second matrix.

    Raises:
        ValueError: If matrices can't be multiplied.

    Returns:
        np.ndarray: The resulting matrix.
    """
    return (np.matmul(m_a, m_b))
