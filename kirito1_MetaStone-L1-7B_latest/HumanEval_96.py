def count_up_to(n):
    """Implement a function that takes an non-negative integer and returns an array of the first n integers that are prime numbers and less than n."""
    if n <= 1:
        return []
    primes = []
    for m in range(2, n):
        is_prime = True
        if m < 2:
            continue
        for i in range(2, int(m ** 0.5) + 1):
            if m % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(m)
    return primes