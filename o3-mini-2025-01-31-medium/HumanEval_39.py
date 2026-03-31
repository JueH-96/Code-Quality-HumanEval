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
        if num == 2:
            return True
        if num % 2 == 0:
            return False
        i = 3
        while i * i <= num:
            if num % i == 0:
                return False
            i += 2
        return True

    # Fibonacci generation starting from 1, 1
    a, b = 1, 1
    count = 0
    while True:
        # We treat the Fibonacci numbers from a (skip ones that are not prime)
        if is_prime(a):
            count += 1
            if count == n:
                return a
        a, b = b, a + b