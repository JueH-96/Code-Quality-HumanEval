def split_words(txt):
    '''
    Given a string of words, return a list of words split on whitespace, if no whitespaces exists in the text you
    should split on commas ',' if no commas exists you should return the number of lower-case letters with odd order in the
    alphabet, ord('a') = 0, ord('b') = 1, ... ord('z') = 25
    Examples
    split_words("Hello world!") ➞ ["Hello", "world!"]
    split_words("Hello,world!") ➞ ["Hello", "world!"]
    split_words("abcdef") == 3 
    '''
    # If there's any whitespace, split on whitespace
    if any(c.isspace() for c in txt):
        return txt.split()
    # If no whitespace but commas exist, split on commas
    if ',' in txt:
        parts = txt.split(',')
        # Filter out any empty strings that may result from leading/trailing commas
        return [p for p in parts if p != '']
    # Otherwise, count lowercase letters with odd order in the alphabet
    count = 0
    for c in txt:
        if 'a' <= c <= 'z':
            if (ord(c) - ord('a')) % 2 == 1:
                count += 1
    return count