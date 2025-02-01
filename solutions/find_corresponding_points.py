import numpy as np

def find_corresponding_points_sol(img1: np.ndarray, img2: np.ndarray) -> np.ndarray:
    """"""
    distances = np.linalg.norm(img1[:, np.newaxis] - img2, axis=2)
    return np.argmin(distances, axis=1)


def find_corresponding_points_sol_2(img1: np.ndarray, img2: np.ndarray) -> np.ndarray:
    """"""
    distances = np.sqrt(np.sum((img1[:, np.newaxis, :] - img2)**2, axis=2))
    return np.argmin(distances, axis=1)
