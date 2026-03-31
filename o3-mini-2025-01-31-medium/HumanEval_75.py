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

    # Generate the list of primes up to a
    primes = [num for num in range(2, a + 1) if is_prime(num)]
    
    # Check all combinations (order matters here, but it's fine for a small range) 
    for p1 in primes:
        for p2 in primes:
            for p3 in primes:
                if p1 * p2 * p3 == a:
                    return True
    return False