def words_string(s):
    """
    Splits a given string into words, using commas and/or spaces as delimiters,
    and returns the resulting list of words.

    Examples:
    >>> words_string("Hi, my name is John")
    ['Hi', 'my', 'name', 'is', 'John']
    >>> words_string("One, two, three, four, five, six")
    ['One', 'two', 'three', 'four', 'five', 'six']
    """
    # Replace commas with spaces, then split on any whitespace
    return s.replace(',', ' ').split()