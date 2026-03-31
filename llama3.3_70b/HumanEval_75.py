def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    def find_prime_factors(n):
        factors = []
        for i in range(2, n + 1):
            if n % i == 0 and is_prime(i):
                factors.append(i)
                n //= i
                if len(factors) == 3:
                    break
        return factors

    prime_factors = find_prime_factors(a)
    return len(prime_factors) == 3 and a == prime_factors[0] * prime_factors[1] * prime_factors[2]