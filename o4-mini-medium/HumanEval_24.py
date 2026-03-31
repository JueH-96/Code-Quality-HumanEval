def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    if n <= 1:
        return 1
    # Look for the smallest divisor > 1; its pair will be the largest proper divisor.
    limit = int(n**0.5)
    for i in range(2, limit + 1):
        if n % i == 0:
            return n // i
    # If no divisor found, n is prime and its largest proper divisor is 1.
    return 1