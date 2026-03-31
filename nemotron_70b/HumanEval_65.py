def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    num_str = str(x)
    num_digits = len(num_str)
    effective_shift = shift % num_digits
    if effective_shift == 0:
        return num_str
    elif effective_shift >= (num_digits // 2):
        return num_str[::-1]
    else:
        return num_str[-effective_shift:] + num_str[:-effective_shift]