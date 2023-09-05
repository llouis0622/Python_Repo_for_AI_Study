def one_hot(val, dim):
    return [np.eye(dim)[_] for _ in val]


def one_hot_encoding(vec):
    vec_dim = vec.shape[1]
    vec_argmax = np.argmax(vec, axis=-1)
    return one_hot(vec_argmax, vec_dim)


def softmax(vec):
    denumerator = np.exp(vec - np.max(vec, axis=-1, keepdims=True))
    numerator = np.sum(denumerator, axis=-1, keepdims=True)
    val = denumerator / numerator
    return val


vec = np.array([[1, 2, 0], [-1, 0, 1], [-10, 0 10]])
print(one_hot_encoding(vec))
print(one_hot_encoding(softmax(vec)))