def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    lower, upper = min(a, b), max(a, b)
    return [num for num in range(lower, upper + 1) if num < 10 and num % 2 == 0]