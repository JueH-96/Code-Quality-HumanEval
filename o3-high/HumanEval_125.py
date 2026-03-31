def split_words(txt):
    '''
    Given a string of words, return a list of words split on whitespace. If no whitespace
    exists in the text, split on commas ','. If no commas exist either, return the number
    of lower-case letters with odd order in the alphabet (a=0, b=1, … z=25).
    '''
    # Case 1: any whitespace present
    if any(ch.isspace() for ch in txt):
        return txt.split()
    
    # Case 2: comma present but no whitespace
    if ',' in txt:
        return txt.split(',')
    
    # Case 3: neither whitespace nor comma – count odd-indexed lower-case letters
    odd_letters = set('bdfhjlnprtvxz')  # letters with odd index in alphabet
    return sum(1 for ch in txt if ch in odd_letters)