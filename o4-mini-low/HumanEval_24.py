def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    if n <= 1:
        return 0
    max_div = 1
    i = 1
    # Loop up to sqrt(n)
    while i * i <= n:
        if n % i == 0:
            j = n // i
            if i < n and i > max_div:
                max_div = i
            if j < n and j > max_div:
                max_div = j
        i += 1
    return max_div