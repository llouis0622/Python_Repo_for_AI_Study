from sklearn.linear_model import LinearRegression


model = LinearRegression()
model.fit(X, y)
y_test = model.predict(x_test)

X_ = np.array([np.append(x, [1]) for x in X])
beta = np.linalg.pinv(X_) @ y
y_test = np.append(x, [1]) @ beta