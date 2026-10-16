import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transposed matrix as a NumPy array.
    """
    # Write code here
    A_T = [[0 for _ in range(len(A))] for _ in range(len(A[-1]))]
    for i in range(len(A)):
        for j in range(len(A[-1])):
            A_T[j][i] = A[i][j]

    return np.array(A_T)