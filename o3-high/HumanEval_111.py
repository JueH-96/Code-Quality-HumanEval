from collections import Counter

def histogram(test):
    """Given a string of space-separated lowercase letters, return a dictionary
    containing the letter(s) that occur the most and their corresponding count.
    If multiple letters share the highest occurrence, include all of them.

    Examples:
    >>> histogram('a b c')
    {'a': 1, 'b': 1, 'c': 1}
    >>> histogram('a b b a')
    {'a': 2, 'b': 2}
    >>> histogram('a b c a b')
    {'a': 2, 'b': 2}
    >>> histogram('b b b b a')
    {'b': 4}
    >>> histogram('')
    {}
    """
    # Split the input string by any whitespace to obtain individual letters.
    letters = test.split()

    # If no letters are found, return an empty dictionary.
    if not letters:
        return {}

    # Count the frequency of each letter.
    counts = Counter(letters)

    # Determine the maximum occurrence count.
    max_count = max(counts.values())

    # Build and return a dictionary with letters that match the maximum count.
    return {letter: cnt for letter, cnt in counts.items() if cnt == max_count}