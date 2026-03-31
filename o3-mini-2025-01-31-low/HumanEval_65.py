def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    x_str = str(x)
    if shift > len(x_str):
        return x_str[::-1]
    # Calculate the split index for circular shifting
    index = len(x_str) - shift
    return x_str[index:] + x_str[:index]