def digitSum(s):
    """Return the sum of ASCII codes of uppercase letters in the given string.

    Args:
        s (str): Input string.

    Returns:
        int: Sum of ASCII codes of uppercase letters.

    Examples:
        >>> digitSum("")
        0
        >>> digitSum("abAB")
        131
        >>> digitSum("abcCd")
        67
        >>> digitSum("helloE")
        69
        >>> digitSum("woArBld")
        131
        >>> digitSum("aAaaaXa")
        153
    """
    return sum(ord(ch) for ch in s if 'A' <= ch <= 'Z')