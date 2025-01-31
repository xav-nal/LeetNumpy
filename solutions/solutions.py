# solutions/solutions.py
import numpy as np

def rotate_matrix_90_sol(matrix: np.ndarray) -> np.ndarray:
    """Transpose and flip rows to rotate 90 degrees clockwise"""
    return np.flip(matrix.T, axis=1)