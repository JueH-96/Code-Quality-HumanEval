def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    if a < 2:
        return False

    prime_count = 0

    # Factor out 2s
    while a % 2 == 0:
        a //= 2
        prime_count += 1

    # Factor out odd primes
    factor = 3
    while factor * factor <= a:
        while a % factor == 0:
            a //= factor
            prime_count += 1
        factor += 2

    # If there's anything left of a, it's a prime
    if a > 2:
        prime_count += 1

    return prime_count == 3