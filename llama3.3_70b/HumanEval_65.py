def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    # Convert the integer to a list of characters for easier manipulation
    x_str = str(x)
    
    # Calculate the effective shift, taking into account cases where shift > number of digits
    effective_shift = shift % len(x_str)
    
    # Perform the circular shift
    if effective_shift == 0:
        return x_str
    else:
        # Split the string at the shift point and reverse the order of the parts
        shifted_str = x_str[-effective_shift:] + x_str[:-effective_shift]
        
    return shifted_str