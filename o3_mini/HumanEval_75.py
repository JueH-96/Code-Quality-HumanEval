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

    original = a
    prime_factors_count = 0
    factor = 2

    while a > 1:
        if a % factor == 0:
            if is_prime(factor):
                prime_factors_count += 1
            a //= factor
        else:
            factor += 1
    
    return prime_factors_count == 3