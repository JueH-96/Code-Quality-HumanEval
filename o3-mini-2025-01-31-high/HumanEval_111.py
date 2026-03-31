def histogram(test):
    """Given a string representing a space separated lowercase letters, return a dictionary
    of the letter with the most repetition and containing the corresponding count.
    If several letters have the same occurrence, return all of them.
    
    Example:
    histogram('a b c') == {'a': 1, 'b': 1, 'c': 1}
    histogram('a b b a') == {'a': 2, 'b': 2}
    histogram('a b c a b') == {'a': 2, 'b': 2}
    histogram('b b b b a') == {'b': 4}
    histogram('') == {}
    """
    if not test:
        return {}
    
    # Split the string into letters and count frequencies
    freq = {}
    for letter in test.split():
        freq[letter] = freq.get(letter, 0) + 1
    
    if not freq:
        return {}
    
    # Identify the maximum frequency found
    max_count = max(freq.values())
    
    # Build result dictionary with only letters that have count equal to max_count
    return {letter: count for letter, count in freq.items() if count == max_count}