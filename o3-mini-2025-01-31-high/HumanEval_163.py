def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    low, high = min(a, b), max(a, b)
    even_digits = [0, 2, 4, 6, 8]
    return [digit for digit in even_digits if low <= digit <= high]