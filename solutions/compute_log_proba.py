import numpy as np

def compute_log_proba_sol(X, mean, sigma):
    n = X.shape[0]
    d = X.shape[1]
    dxm = X - mean
    frac_term = - np.log(2 * np.pi) * (d / 2) - 0.5 * np.log(np.linalg.det(sigma))
    exp_term = -0.5 * np.sum(dxm * np.dot(dxm, np.linalg.inv(sigma)), axis=1)
    log_p = frac_term + exp_term
    return  log_p