def fibfib(n: int):
    if n < 3:
        return 0 if n != 2 else 1

    a, b, c = 0, 0, 1
    for _ in range(3, n + 1):
        a, b, c = b, c, a + b + c
    return c