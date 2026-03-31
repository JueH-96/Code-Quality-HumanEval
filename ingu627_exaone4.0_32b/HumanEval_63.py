def fibfib(n: int):
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 1
    a, b, c = 0, 0, 1  # Represents fibfib(0), fibfib(1), fibfib(2)
    for _ in range(3, n + 1):
        next_val = a + b + c
        a, b, c = b, c, next_val
    return c