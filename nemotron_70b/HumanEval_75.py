def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    
    def is_prime(n):
        """Check if number is prime."""
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    # Generate all prime numbers less than 100
    primes = [i for i in range(2, 100) if is_prime(i)]
    
    # Check all combinations of three prime numbers
    for i in primes:
        for j in primes:
            for k in primes:
                if i * j * k == a:
                    return True
    return False