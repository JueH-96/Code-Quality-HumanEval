def fib4(n: int):
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 2
    elif n == 3:
        return 0

    a, b, c, d = 2, 0, 4, 8
    for i in range(4, n):
        e = a + b + c + d
        a, b, c, d = b, c, d, e
    return d