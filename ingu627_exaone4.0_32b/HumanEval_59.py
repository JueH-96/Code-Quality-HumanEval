def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    largest_factor = 1
    # Divide by 2 until n is odd
    while n % 2 == 0:
        largest_factor = 2
        n = n // 2
    # Now n must be odd
    i = 3
    while i * i <= n:
        while n % i == 0:
            largest_factor = i
            n = n // i
        i += 2
    # If n is a prime number greater than 2
    if n > 2:
        largest_factor = n
    return largest_factor