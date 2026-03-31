import re

def anti_shuffle(s):
    """
    Write a function that takes a string and returns an ordered version of it.
    Ordered version of string, is a string where all words (separated by space)
    are replaced by a new word where all the characters arranged in
    ascending order based on ascii value.
    Note: You should keep the order of words and blank spaces in the sentence.

    For example:
    anti_shuffle('Hi') returns 'Hi'
    anti_shuffle('hello') returns 'ehllo'
    anti_shuffle('Hello World!!!') returns 'Hello !!!Wdlor'
    """
    # Split the string preserving the spaces using regex.
    tokens = re.split(r'(\s+)', s)
    
    # Process only non-space tokens (words)
    result = []
    for token in tokens:
        if token and not token.isspace():
            result.append(''.join(sorted(token)))
        else:
            result.append(token)
    return ''.join(result)