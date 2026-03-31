def string_sequence(n: int) -> str:
    """Return a string containing space-delimited numbers starting from 0 up to n inclusive.
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    """
    if n < 0:
        # If n is negative, we'll return an empty string (or you could raise ValueError)
        # The original examples don't specify behavior for negatives, but this is a safe fallback.
        return ''
    return ' '.join(str(i) for i in range(n + 1))