import numpy as np
from collections import Counter

def bag_of_words_vector(tokens, vocab):
    """
    Returns: np.ndarray of shape (len(vocab),), dtype=int
    """
    token_count = Counter(tokens)

    vector = np.zeros(len(vocab), dtype = int)

    for i , word in enumerate(vocab):
        vector[i] = token_count.get(word,0)

    return vector
    pass