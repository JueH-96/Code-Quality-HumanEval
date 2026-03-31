def fib4(n):
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 2
    elif n == 3:
        return 0
    else:
        a, b, c, d = 0, 0, 2, 0  # Represents fib4(0) to fib4(3)
        for i in range(4, n + 1):
            next_fib = a + b + c + d
            a, b, c, d = b, c, d, next_fib
        return d