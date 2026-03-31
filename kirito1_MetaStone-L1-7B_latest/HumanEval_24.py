import math

def largest_divisor(n):
    if n < 2:
        return None
    max_div = 1
    sqrt_n = math.isqrt(n)
    for i in range(2, sqrt_n + 1):
        if n % i == 0:
            candidate = n // i
            if candidate < n and candidate > max_div:
                max_div = candidate
    return max_div