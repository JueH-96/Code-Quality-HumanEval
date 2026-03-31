def special_factorial(n):
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    total = 1
    current_fact = 1
    for i in range(1, n + 1):
        current_fact *= i
        total *= current_fact
    return total