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
    
    factor_count = 0
    n = a
    for p in range(2, a + 1):
        if p * p > n:
            break
        while n % p == 0 and is_prime(p):
            factor_count += 1
            n //= p
            if factor_count > 3:
                return False
    if n > 1 and is_prime(n):
        factor_count += 1
    return factor_count == 3