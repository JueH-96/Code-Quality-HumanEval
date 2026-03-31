import re

def is_bored(S):
    """
    You'll be given a string of words, and your task is to count the number
    of boredoms. A boredom is a sentence that starts with the word "I".
    Sentences are delimited by '.', '?' or '!'.
    """
    # Split the text into sentences using '.', '?', '!' as delimiters
    sentences = re.split(r'[.?!]', S)
    
    # Count sentences whose first non-space word is exactly "I"
    return sum(
        1
        for sentence in sentences
        if (sentence := sentence.strip()) and sentence.split()[0] == "I"
    )