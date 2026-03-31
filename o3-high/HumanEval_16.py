def count_distinct_characters(string: str) -> int:
    """Given a string, return the number of distinct characters it contains, case–insensitively.
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    return len(set(string.lower()))