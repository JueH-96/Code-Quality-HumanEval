def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    # split string into groups of three characters
    groups = [s[3 * i:3 * i + 3] for i in range((len(s) + 2) // 3)]
    # reverse the cycling by moving the last character to the beginning for groups of three
    groups = [(group[-1] + group[:-1]) if len(group) == 3 else group for group in groups]
    return "".join(groups)