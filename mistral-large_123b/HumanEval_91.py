def is_bored(S):
    import re
    sentences = re.split(r'[.?!]', S)
    boredoms = sum(1 for sentence in sentences if sentence.strip().startswith("I"))
    return boredoms