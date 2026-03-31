def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    def is_prime(x: int) -> bool:
        if x < 2:
            return False
        for i in range(2, int(x**0.5) + 1):
            if x % i == 0:
                return False
        return True

    largest_factor = None
    for i in range(int(n**0.5) + 1, 1, -1):
        if n % i == 0 and is_prime(i):
            largest_factor = i
            break
    if largest_factor is None:
        # if no prime factor found in the loop (n is a power of a prime), 
        # find the smallest prime factor which will be the only prime factor
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0 and is_prime(i):
                largest_factor = i
                break
        else:
            # if n itself is a prime power of the smallest prime (2)
            largest_factor = n
    return largest_factor