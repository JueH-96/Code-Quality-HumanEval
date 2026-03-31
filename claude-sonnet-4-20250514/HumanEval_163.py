def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    # Ensure a is the smaller value
    start = min(a, b)
    end = max(a, b)
    
    # Find even digits (0, 2, 4, 6, 8) within the range
    result = []
    for digit in [0, 2, 4, 6, 8]:
        if start <= digit <= end:
            result.append(digit)
    
    return result