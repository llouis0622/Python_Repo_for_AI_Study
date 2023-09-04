var = init
grad = gradient(var)
while (norm(grad) > eps):
    var = var - lr * grad
    grad = gradient(var)