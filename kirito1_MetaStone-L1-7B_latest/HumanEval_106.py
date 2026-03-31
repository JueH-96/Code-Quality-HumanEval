import math

def f(n):
    result = []
    for j in range(1, n + 1):
        if j % 2 == 0:
            result.append(math.factorial(j))
        else:
            result.append((j * (j + 1)) // 2)
    return result