def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    groups = [s[i:i+3] for i in range(0, len(s), 3)]
    groups = [g[-1] + g[:-1] if len(g) == 3 else g for g in groups]
    return "".join(groups)