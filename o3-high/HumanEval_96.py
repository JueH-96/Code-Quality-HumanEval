def count_up_to(n):
    """Return a list of all prime numbers strictly less than n."""
    if n < 2:
        return []
    sieve = [True] * n  # indices 0 .. n-1
    sieve[0] = sieve[1] = False
    limit = int(n ** 0.5) + 1
    for i in range(2, limit):
        if sieve[i]:
            sieve[i * i:n:i] = [False] * ((n - i * i - 1) // i + 1)
    return [i for i, is_prime in enumerate(sieve) if is_prime]