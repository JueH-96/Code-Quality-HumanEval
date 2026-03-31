def is_multiply_prime(a):
    primes = [2, 3, 5, 7]
    factors = []
    for p in primes:
        while a % p == 0:
            if p not in factors:
                factors.append(p)
            a /= p
    return len(factors)==3 and a==1