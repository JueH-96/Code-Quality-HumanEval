def is_bored(S):
    """
    You'll be given a string of words, and your task is to count the number
    of boredoms. A boredom is a sentence that starts with the word "I".
    Sentences are delimited by '.', '?' or '!'.
   
    For example:
    >>> is_bored("Hello world")
    0
    >>> is_bored("The sky is blue. The sun is shining. I love this weather")
    1
    """
    import re
    # Split the string by sentence delimiters . ? !
    sentences = re.split(r'[.?!]', S)
    count = 0
    for sentence in sentences:
        # Remove leading/trailing whitespace
        stripped_sentence = sentence.strip()
        if not stripped_sentence:
            continue
        # Check if the sentence starts with "I" as a full word.
        # Split the sentence on whitespace and check first token.
        words = stripped_sentence.split()
        if words and words[0] == 'I':
            count += 1
    return count