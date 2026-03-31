def prime_fib(n: int):
    """
    prime_fib returns the n-th number that is both a Fibonacci number and prime.

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
    if not isinstance(n, int) or n < 1:
        raise ValueError("n must be a positive integer")

    def is_prime(num: int) -> bool:
        if num < 2:
            return False
        small_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
        for p in small_primes:
            if num == p:
                return True
            if num % p == 0:
                return False

        # Write n−1 as 2^s * d with d odd (by factoring out powers of 2 from n − 1)
        d = num - 1
        s = 0
        while d % 2 == 0:
            d //= 2
            s += 1

        # Miller–Rabin deterministic bases depending on num’s size
        if num < 2_047:
            bases = [2]
        elif num < 1_373_653:
            bases = [2, 3]
        elif num < 9_080_191:
            bases = [31, 73]
        elif num < 25_326_001:
            bases = [2, 3, 5]
        elif num < 3_474_749_660_383:
            bases = [2, 3, 5, 7, 11, 13]
        elif num < 341_550_071_728_321:
            bases = [2, 3, 5, 7, 11, 13, 17]
        elif num < 3_825_123_056_546_413_051:
            bases = [2, 3, 5, 7, 11, 13, 17, 19, 23]
        else:
            bases = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]

        def check(a: int) -> bool:
            x = pow(a, d, num)
            if x == 1 or x == num - 1:
                return True
            for _ in range(s - 1):
                x = pow(x, 2, num)
                if x == num - 1:
                    return True
            return False

        return all(check(a) for a in bases if a % num)

    count = 0
    a, b = 0, 1  # Fibonacci starting values F0, F1
    while True:
        a, b = b, a + b  # advance to next Fibonacci number
        if is_prime(a):
            count += 1
            if count == n:
                return a