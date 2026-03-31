def anti_shuffle(s):
    import re
    # Use regex to split by spaces while preserving them.
    tokens = re.split(r'(\s+)', s)
    result = []
    for token in tokens:
        # if token is only whitespace, append it as is.
        if token.isspace():
            result.append(token)
        else:
            # Sort each character in token according to ascii value.
            sorted_token = ''.join(sorted(token))
            result.append(sorted_token)
    return ''.join(result)