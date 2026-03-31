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
        """Check if a number is prime."""
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def fibonacci():
        """Generate Fibonacci numbers on the fly."""
        a, b = 0, 1
        while True:
            yield a
            a, b = b, a + b

    fib_gen = fibonacci()
    prime_fib_count = 0
    while True:
        num = next(fib_gen)
        if is_prime(num):
            prime_fib_count += 1
            if prime_fib_count == n:
                return num