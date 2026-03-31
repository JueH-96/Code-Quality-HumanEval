def is_bored(S):
    """
    You'll be given a string of words, and your task is to count the number
    of boredoms. A boredom is a sentence that starts with the word "I".
    Sentences are delimited by '.', '?' or '!'.
    """
    import re
    sentences = re.split(r'[.?!]', S)
    count = 0
    for s in sentences:
        words = s.strip().split()
        if words and words[0] == "I":
            count += 1
    return count