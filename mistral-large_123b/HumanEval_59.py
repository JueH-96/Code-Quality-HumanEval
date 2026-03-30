def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    largest = None
    factor = 2
    while n != 1:
        if n % factor == 0 and is_prime(factor):
            largest = factor
            while n % factor == 0:
                n //= factor
        factor += 1
    return largest