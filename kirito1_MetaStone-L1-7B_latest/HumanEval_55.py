def fib(n: int):
    """Return nth Fibonacci number."""
    if n == 1 or n == 2:
        return 1
    a, b = 1, 1
    for i in range(3, n + 1):
        c = a + b
        a = b
        b = c
    return b