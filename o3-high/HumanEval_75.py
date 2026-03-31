def is_multiply_prime(a):
    """Return True if `a` equals the product of exactly three prime numbers
    (primes may repeat), otherwise return False.
    Assumes a is an integer.
    """
    if a < 2:
        return False

    count = 0
    n = a
    p = 2

    while p * p <= n and count <= 3:
        while n % p == 0:
            n //= p
            count += 1
            if count > 3:          # More than 3 prime factors ⇒ not valid
                return False
        p += 1

    if n > 1:
        count += 1

    return count == 3