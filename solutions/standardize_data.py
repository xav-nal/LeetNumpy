# solutions/2_standardize_data.py
import numpy as np

def standardize_sol(x: np.ndarray) -> np.ndarray:
    centered_data = x - np.mean(x, axis=0)    
    std_data = centered_data / np.std(centered_data, axis=0)
    return std_data