def prime_fib(n: int):
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    >>> prime_fib(1)
    2
    >>> prime_fib(2)
    3
    >>> prime_fib(3)
    5
    >>> prime_fib(4)
    13
    >>> prime_fib(5)
    89
    """
    def is_prime(x: int) -> bool:
        if x < 2:
            return False
        # small primes trial division
        for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29):
            if x == p:
                return True
            if x % p == 0:
                return False
        # Miller-Rabin deterministic bases for <2^64
        d, s = x - 1, 0
        while d % 2 == 0:
            d //= 2
            s += 1
        for a in (2, 325, 9375, 28178, 450775, 9780504, 1795265022):
            if a % x == 0:
                continue
            y = pow(a, d, x)
            if y == 1 or y == x - 1:
                continue
            for _ in range(s - 1):
                y = pow(y, 2, x)
                if y == x - 1:
                    break
            else:
                return False
        return True

    if n < 1:
        raise ValueError("n must be a positive integer")
    count = 0
    a, b = 0, 1
    while True:
        a, b = b, a + b
        if is_prime(a):
            count += 1
            if count == n:
                return a