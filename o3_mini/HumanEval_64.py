def vowels_count(s):
    """Write a function vowels_count which takes a string representing
    a word as input and returns the number of vowels in the string.
    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. Here, 'y' is also a
    vowel, but only when it is at the end of the given word.

    Example:
    >>> vowels_count("abcde")
    2
    >>> vowels_count("ACEDY")
    3
    """
    vowels = {'a', 'e', 'i', 'o', 'u'}
    if not s:
        return 0
    
    count = 0
    # Count vowels for all characters except possibly the last one.
    for char in s[:-1]:
        if char.lower() in vowels:
            count += 1
    # For the last character, count if it's one of the vowels or if it's 'y'
    last_char = s[-1]
    if last_char.lower() in vowels or last_char.lower() == 'y':
        count += 1
    return count