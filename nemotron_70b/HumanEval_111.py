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
    # Split the input string into a list of letters
    letters = test.split()
    
    # Create a dictionary to store letter frequencies
    freq_dict = {}
    
    # Iterate over each letter and update its frequency in the dictionary
    for letter in letters:
        if letter in freq_dict:
            freq_dict[letter] += 1
        else:
            freq_dict[letter] = 1
    
    # If the input string is empty, return an empty dictionary
    if not freq_dict:
        return {}
    
    # Find the maximum frequency
    max_freq = max(freq_dict.values())
    
    # Filter the dictionary to include only letters with the maximum frequency
    result = {letter: freq for letter, freq in freq_dict.items() if freq == max_freq}
    
    return result