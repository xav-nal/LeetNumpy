import numpy as np

def rotate_and_concatenate_sol(matrix: np.ndarray) -> np.ndarray:
    """Rotate a 2D matrix by 90, 180, and 270 degrees and concatenate them horizontally."""
    
    rotated_90 = np.fliplr(matrix.T)
    rotated_180 = np.flipud(np.fliplr(matrix))
    rotated_270 = np.flipud(matrix.T)
    
    return np.hstack((rotated_90, rotated_180, rotated_270))