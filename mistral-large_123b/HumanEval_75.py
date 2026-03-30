def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100.
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def prime_factors(n):
        factors = []
        divisor = 2
        while n > 1 and divisor <= int(n**0.5) + 1:
            if n % divisor == 0 and is_prime(divisor):
                factors.append(divisor)
                n //= divisor
            else:
                divisor += 1
        if n > 1:
            factors.append(n)
        return factors

    primes = prime_factors(a)
    return len(primes) == 3 and all(is_prime(p) for p in primes)