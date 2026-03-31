import math

def is_prime(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        max_divisor = math.isqrt(n)
        for i in range(3, max_divisor + 1, 2):
            if n % i == 0:
                return False
        return True