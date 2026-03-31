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

    # Helper to test primality; small n only
    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    # Factor count with multiplicity
    n = a
    count = 0

    # Count factors of 2
    while n % 2 == 0:
        count += 1
        n //= 2
        if count > 3:
            return False

    # Count odd factors
    d = 3
    while d * d <= n:
        while n % d == 0:
            if not is_prime(d):
                return False
            count += 1
            n //= d
            if count > 3:
                return False
        d += 2

    # If remainder is prime
    if n > 1:
        if not is_prime(n):
            return False
        count += 1

    return count == 3