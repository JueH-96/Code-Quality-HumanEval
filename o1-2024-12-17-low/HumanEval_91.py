def is_bored(S):
    """
    You'll be given a string of words, and your task is to count the number
    of boredoms. A boredom is a sentence that starts with the word "I".
    Sentences are delimited by '.', '?' or '!'.
    """
    import re
    count = 0
    sentences = re.split(r'[.?!]', S)
    for sent in sentences:
        words = sent.strip().split()
        if words and words[0] == 'I':
            count += 1
    return count