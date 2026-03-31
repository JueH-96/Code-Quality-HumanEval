def is_multiply_prime(a):
    if a < 2:
        return False
    count = 0
    n = a
    i = 2
    while i * i <= n:
        while n % i == 0:
            count += 1
            if count > 3:
                return False
            n //= i
        i += 1
    if n > 1:
        count += 1
    return count == 3