def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    # split string into groups of length 3
    groups = [s[i:i+3] for i in range(0, len(s), 3)]
    # reverse the cyclic shift for groups of length exactly 3
    decoded_groups = [(group[-1] + group[:-1]) if len(group) == 3 else group for group in groups]
    return "".join(decoded_groups)