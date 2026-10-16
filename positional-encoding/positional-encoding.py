import numpy as np

def positional_encoding(seq_len: int, d_model: int, base: float = 10000.0) -> np.ndarray:
    """
    Returns a NumPy array of shape (seq_len, d_model).
    """
    # Write code here
    PE = np.zeros((seq_len, d_model))
    for pos in range(seq_len):
        for i in range(d_model):
            normalized_pos = pos/(base**((2*i)/d_model))
            if 2*i < d_model:                
                PE[pos, 2*i] = np.sin(normalized_pos)
            if 2*i+1 < d_model:
                PE[pos, 2*i + 1] = np.cos(normalized_pos)

    return PE