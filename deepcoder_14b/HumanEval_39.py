def is_prime(k):
    """Check if a number k is a prime."""
    if k <= 1:
        return False
    if k == 2:
        return True
    if k % 2 == 0:
        return False
    for i in range(3, int(k ** 0.5) + 1, 2):
        if k % i == 0:
            return False
    return True

def nth_prime_fib(n):
    """Return the nth prime number in the Fibonacci sequence."""
    fib_primes = []
    prev, curr = 0, 1
    while len(fib_primes) < n:
        if is_prime(curr):
            fib_primes.append(curr)
        # Generate next Fibonacci number
        next_fib = prev + curr
        prev = curr
        curr = next_fib
    return fib_primes[-1]

# Example usage:
# To find the 5th prime in Fibonacci sequence, call nth_prime_fib(5)