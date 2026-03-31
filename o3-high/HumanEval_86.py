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
    res = []
    current_word = []
    
    for ch in s:
        if ch.isspace():
            if current_word:
                res.append(''.join(sorted(current_word)))
                current_word.clear()
            res.append(ch)  # Preserve the whitespace character(s)
        else:
            current_word.append(ch)
    
    if current_word:
        res.append(''.join(sorted(current_word)))
    
    return ''.join(res)