def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    # Convert to string to work with digits
    digits = str(x)
    n = len(digits)
    
    # If shift is greater than number of digits, return reversed
    if shift > n:
        return digits[::-1]
    
    # Handle case where shift is 0 or multiple of n
    shift = shift % n
    
    # Circular shift right: take last 'shift' digits and put them at front
    # then take remaining digits and put them at end
    return digits[-shift:] + digits[:-shift]