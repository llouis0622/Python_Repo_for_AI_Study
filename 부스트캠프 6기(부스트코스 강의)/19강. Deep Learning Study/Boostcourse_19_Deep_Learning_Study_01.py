def softmax(vec):
    denumerator = np.exp(vec - np.max(vec, axis=-1, keepdims=True))
    numerator = np.sum(denumerator, axis=-1, keepdims=True)
    val = denumerator / numerator
    return val


vec = np.array([[1, 2, 0], [-1, 0, 1], [-10, 0 10]])
softmax(vec)