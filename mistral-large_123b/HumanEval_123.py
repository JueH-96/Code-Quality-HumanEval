def get_odd_collatz(n):
    collatz = []
    while n != 1:
        if n % 2 != 0:
            collatz.append(n)
        n = (3 * n + 1) if n % 2 else n // 2
    collatz.append(1)
    return sorted(collatz)