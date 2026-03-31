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
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    # Iterate over all pairs of possible primes for the first two factors.
    for p in range(2, a + 1):
        if is_prime(p):
            for q in range(2, a + 1):
                if is_prime(q) and p * q <= a and a % (p * q) == 0:
                    r = a // (p * q)
                    if is_prime(r):
                        # Ensure that we indeed have three factors whose multiplication gives a.
                        if p * q * r == a:
                            return True
    return False