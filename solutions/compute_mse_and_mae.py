import numpy as np

def compute_mse_and_mae_sol(y: np.ndarray, x: np.ndarray, w: np.ndarray) -> tuple:
    error = y - x.dot(w)
    mse = 1 / 2 * np.mean(error ** 2)
    mae = np.mean(np.abs(error))
    return (mse, mae)