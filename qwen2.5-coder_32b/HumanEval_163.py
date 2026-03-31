def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    # Ensure a is less than or equal to b
    start, end = min(a, b), max(a, b)
    
    # Generate even numbers between start and end inclusive
    even_numbers = [num for num in range(start, end + 1) if num % 2 == 0]
    
    return even_numbers