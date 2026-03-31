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
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    if a < 0:
        return False

    # Generate list of candidate primes less than or equal to a.
    primes = [x for x in range(2, a+1) if is_prime(x)]
    
    # Check all combinations (allowing repetition)
    for p in primes:
        if a % p != 0:
            continue
        for q in primes:
            if (a // p) % q != 0:
                continue
            r = a // (p * q)
            if r < 2:
                continue
            if is_prime(r) and p * q * r == a:
                return True
    return False