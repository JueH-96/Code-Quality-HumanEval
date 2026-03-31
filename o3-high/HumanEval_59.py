def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    if n <= 1:
        raise ValueError("n must be greater than 1")

    # Remove factors of 2 first
    largest = None
    while n % 2 == 0:
        largest = 2
        n //= 2

    # Check odd factors starting from 3
    factor = 3
    while factor * factor <= n:
        while n % factor == 0:
            largest = factor
            n //= factor
        factor += 2  # Only test odd numbers

    # If what's left is greater than 2, it is a prime factor itself
    if n > 2:
        largest = n

    return largest