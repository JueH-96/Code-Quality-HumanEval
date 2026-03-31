def encode(s):
    encoded = []
    i = 0
    while i < len(s):
        group = s[i:i+3]
        if len(group) == 3:
            # Rotate left once: move first character to end
            encoded_group = group[1:] + group[0]
        else:
            encoded_group = group
        encoded.append(encoded_group)
        i += 3
    return ''.join(encoded)

def decode(s):
    decoded = []
    i = 0
    while i < len(s):
        group = s[i:i+3]
        if len(group) == 3:
            # Rotate right once: move last character to front
            decoded_group = group[-1] + group[:-1]
        else:
            decoded_group = group
        decoded.append(decoded_group)
        i += 3
    return ''.join(decoded)