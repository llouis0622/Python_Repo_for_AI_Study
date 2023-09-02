X = np.array([[1, -2, 3], 
              [7, 5, 0], 
            [-2, -1, 2]])

Y = np.array([[0, 1], 
              [1, -1], 
              [-2, 1]])

X @ Y
np.inner(X, Y)
np.linalg.inv(X)