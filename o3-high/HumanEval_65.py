def circular_shift(x, shift):
    """Circular shift the digits of the integer x to the right by `shift`
    positions and return the result as a string.

    If `shift` is greater than the number of digits, return the digits reversed.

    >>> circular_shift(12, 1)
    '21'
    >>> circular_shift(12, 2)
    '12'
    """
    s = str(abs(x))
    n = len(s)

    if shift > n:
        shifted = s[::-1]
    else:
        if shift == 0 or n == 0:
            shifted = s
        else:
            shift %= n  # ensure shift is within bounds
            shifted = s[-shift:] + s[:-shift]

    return ('-' if x < 0 else '') + shifted