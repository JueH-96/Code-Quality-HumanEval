def vowels_count(s):
    """
    Counts the number of vowels in the given string.

    The vowels considered are 'a', 'e', 'i', 'o', 'u' (case–insensitive).
    In addition, 'y' (or 'Y') is considered a vowel only when it appears
    as the final character of the string.

    Parameters
    ----------
    s : str
        The input word to inspect.

    Returns
    -------
    int
        The number of vowels found in the input word.

    Examples
    --------
    >>> vowels_count("abcde")
    2
    >>> vowels_count("ACEDY")
    3
    """
    vowels = set('aeiou')
    n = len(s)
    count = 0
    for i, ch in enumerate(s):
        ch_low = ch.lower()
        if ch_low in vowels:
            count += 1
        elif ch_low == 'y' and i == n - 1:
            count += 1
    return count