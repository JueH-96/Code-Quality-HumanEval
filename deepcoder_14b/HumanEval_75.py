def is_semiprime(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    if n < 4:  # The smallest semiprime is 4 (2*2)
        return False

    sqrt_n = int(n ** 0.5)

    for p in range(2, sqrt_n + 1):
        if is_prime(p) and n % p == 0:
            q = n // p
            if is_prime(q):
                return True
    return False