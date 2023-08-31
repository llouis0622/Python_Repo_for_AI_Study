def scalar_vector_product(scalar, vector):
    result = []
    for value in vector:
        result.append(scalar * value)
    return result


iternation_max = 100000000

vector = list(range(iternation_max))
scalar = 2

%timeit scalar_vector_product(scalar, vector)
%timeit [scalar * value for value in range(iternation_max)]
%timeit np.arange(iternation_max) * scalar