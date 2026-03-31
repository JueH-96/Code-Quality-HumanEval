def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    def is_prime(n):
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        i = 3
        while i * i <= n:
            if n % i == 0:
                return False
            i += 2
        return True

    # factor a and count primes with multiplicity
    n = a
    count = 0
    # check factor 2
    while n % 2 == 0:
        count += 1
        n //= 2
    # check odd factors
    p = 3
    while p * p <= n:
        while n % p == 0:
            if not is_prime(p):
                break
            count += 1
            n //= p
        p += 2
    # if remainder is a prime >1
    if n > 1:
        count += 1
    return count == 3