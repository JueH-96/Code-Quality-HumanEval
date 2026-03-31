import math

def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    """
    def is_prime(num):
        if num <= 1:
            return False
        if num <= 3:
            return True
        if num % 2 == 0 or num % 3 == 0:
            return False
        limit = int(math.isqrt(num))
        i = 5
        while i <= limit:
            if num % i == 0 or num % (i + 2) == 0:
                return False
            i += 6
        return True

    return x if is_prime(n) else y