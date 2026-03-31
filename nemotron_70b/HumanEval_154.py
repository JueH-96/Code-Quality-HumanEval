def cycpattern_check(a, b):
    """
    Checks if the second word or any of its rotations is a substring in the first word.

    Args:
        a (str): The string to search in.
        b (str): The pattern to search for.

    Returns:
        bool: True if b or any rotation of b is found in a, False otherwise.
    """
    def rotate(s):
        """Generate all rotations of a given string."""
        return [s[i:] + s[:i] for i in range(len(s))]

    # Generate all rotations of pattern 'b'
    rotations = rotate(b)

    # Check if any rotation is a substring of 'a'
    return any(r in a for r in rotations)