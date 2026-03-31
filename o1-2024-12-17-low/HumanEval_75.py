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
    
    count_factors = 0
    temp = a
    
    for candidate in range(2, 100):  # 100 is safe since a < 100
        while temp % candidate == 0 and is_prime(candidate):
            temp //= candidate
            count_factors += 1
            if count_factors > 3:
                return False
        if temp == 1:
            break
            
    return count_factors == 3