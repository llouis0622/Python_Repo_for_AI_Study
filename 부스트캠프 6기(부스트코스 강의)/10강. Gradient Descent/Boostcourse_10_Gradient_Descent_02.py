var = init
grad = gradient(var)
while (abs(grad) > eps):
    var = var - lr * grad
    grad = gradient(var)