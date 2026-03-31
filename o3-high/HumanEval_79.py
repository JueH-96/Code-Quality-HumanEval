def decimal_to_binary(decimal):
    """Convert a non-negative integer in decimal form to a binary string
    wrapped with 'db' at both the start and the end.

    Examples
    --------
    >>> decimal_to_binary(15)
    'db1111db'
    >>> decimal_to_binary(32)
    'db100000db'
    >>> decimal_to_binary(0)
    'db0db'
    """
    if not isinstance(decimal, int):
        raise TypeError("Input must be an integer.")
    if decimal < 0:
        raise ValueError("Input must be a non-negative integer.")

    binary_digits = bin(decimal)[2:]  # strip the '0b' prefix
    return f"db{binary_digits}db"