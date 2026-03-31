def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    even_digits = [2, 4, 6, 8]
    start = min(a, b)
    end = max(a, b)
    return [digit for digit in even_digits if start <= digit <= end]