import numpy as np

def pad_sequences(seqs: list, pad_value: int = 0, max_len: int | None = None) -> np.ndarray:
    """
    Returns: np.ndarray of shape (N, L) where:
      N = len(seqs)
      L = max_len if provided else max(len(seq) for seq in seqs) or 0
    """
    # Your code here
    if len(seqs) == 0:
        tmp = np.array(seqs, dtype=int)
        tmp.shape = (0, 0)
        return tmp
    if max_len is None:
        max_len = max(len(seq) for seq in seqs)
    
    return np.array([seqs[i] + [pad_value]*(max_len-len(seqs[i])) if len(seqs[i]) < max_len else seqs[i][:max_len] for i in range(len(seqs))])