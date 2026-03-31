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
    s = s.lower()  # convert to lowercase for simplicity
    count = sum(1 for char in s[:-1] if char in 'aeiou')  # count vowels excluding last character
    if s and s[-1].lower() in 'yaeiou':  # check if last character is 'y' or any other vowel
        count += 1
    return count