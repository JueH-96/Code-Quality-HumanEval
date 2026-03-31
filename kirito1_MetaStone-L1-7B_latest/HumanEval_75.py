import math

def is_multiply_prime(a):
    if a < 2:
        return False
    
    def prime_factors(n):
        factors = []
        # Check for divisibility by 2
        while n % 2 == 0:
            factors.append(2)
            n = n // 2
        # Now check odd numbers starting from 3 up to sqrt(n)
        i = 3
        max_factor = math.sqrt(n)
        while i <= max_factor and n > 1:
            while n % i == 0:
                factors.append(i)
                n = n // i
                if n > 1:
                    max_factor = math.sqrt(n)  # Update the maximum factor after division
            i += 2
        # If remaining n is a prime number greater than 2
        if n > 1:
            factors.append(n)
        return factors
    
    factors = prime_factors(a)
    return len(factors) == 3