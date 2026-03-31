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
    import re
    # Split the string while preserving whitespace
    tokens = re.split(r'(\s+)', s)
    result = []
    for token in tokens:
        # If it's whitespace, keep it as is
        if token.isspace() or token == "":
            result.append(token)
        else:
            sorted_token = "".join(sorted(token))
            result.append(sorted_token)
    return "".join(result)