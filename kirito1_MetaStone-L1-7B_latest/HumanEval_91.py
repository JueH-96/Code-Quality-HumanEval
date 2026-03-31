import re

def is_bored(S):
    sentences = re.split(r'[.!?]', S)
    count = 0
    for s in sentences:
        if not s.strip():  # Skip empty strings resulting from split
            continue
        trimmed_s = s.lstrip()
        if len(trimmed_s) == 0:
            continue
        if trimmed_s[0] == 'I':
            count += 1
    return count