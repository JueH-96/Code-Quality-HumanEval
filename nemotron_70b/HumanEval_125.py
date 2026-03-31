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
    # First, try to split on whitespace
    words = txt.split()
    
    # If no whitespaces exist, the list will contain the original string as a single element
    if len(words) == 1:
        # Try to split on commas
        words = txt.split(',')
        
        # If still only one element, it means no commas either
        if len(words) == 1:
            # Count the number of lowercase letters with odd order in the alphabet
            return sum(1 for char in txt.lower() if char.isalpha() and ord(char) % 2 != 0)
    
    # If we've reached this point, we have a list of words (either from whitespace or comma splitting)
    return words