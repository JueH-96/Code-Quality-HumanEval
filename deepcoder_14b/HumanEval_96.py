def count_up_to(n):
    def is_prime(k):
        if k < 2:
            return False
        for i in range(2, int(k ** 0.5) + 1):
            if k % i == 0:
                return False
        return True

    primes = []
    if n <= 2:
        return primes
    for number in range(2, n):
        if is_prime(number):
            primes.append(number)
    return primes