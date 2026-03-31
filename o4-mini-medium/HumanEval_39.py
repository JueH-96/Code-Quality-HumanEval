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
    def is_prime(num: int) -> bool:
        if num < 2:
            return False
        small_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        for p in small_primes:
            if num == p:
                return True
            if num % p == 0:
                return False
        # Miller-Rabin deterministic for 64-bit integers
        d, s = num - 1, 0
        while d % 2 == 0:
            d //= 2
            s += 1
        bases = [2, 325, 9375, 28178, 450775, 9780504, 1795265022]
        for a in bases:
            if a % num == 0:
                continue
            x = pow(a, d, num)
            if x == 1 or x == num - 1:
                continue
            for _ in range(s - 1):
                x = pow(x, 2, num)
                if x == num - 1:
                    break
            else:
                return False
        return True

    if n <= 0:
        raise ValueError("n must be a positive integer")
    count = 0
    a, b = 0, 1
    while True:
        a, b = b, a + b
        if is_prime(b):
            count += 1
            if count == n:
                return b