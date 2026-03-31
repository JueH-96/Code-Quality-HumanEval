import math
def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n ≥ 1 and is not a prime."""
    
    def is_prime(num):
        if num == 2 or num == 3: return True
        if num < 2 or num % 2 == 0: return False
        for i in range(3, int(math.sqrt(num)) + 1, 2):
            if num % i == 0:
                return False
        return True
    
    max_prime = -1
    while n % 2 == 0:
        max_prime = 2
        n >>= 1
    
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i== 0:
            max_prime = i
            n = n / i
            
    if n > 2 and is_prime(n):
        max_prime = n
        
    return int(max_prime)