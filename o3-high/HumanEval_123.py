def get_odd_collatz(n):
    """
    Given a positive integer n, return a sorted list containing the odd numbers
    encountered in the Collatz sequence starting at n and ending at 1 (inclusive).
    """
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input must be a positive integer.")

    odds = set()

    while True:
        if n % 2 == 1:
            odds.add(n)
        if n == 1:
            break
        n = n // 2 if n % 2 == 0 else 3 * n + 1

    return sorted(odds)