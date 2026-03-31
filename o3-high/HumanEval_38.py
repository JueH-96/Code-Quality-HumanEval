def decode_cyclic(s: str):
    """
    Takes as input a string encoded with the encode_cyclic function and returns the decoded string.
    """
    # Split the encoded string into the same groups of length 3 (last group may be shorter)
    groups = [s[3 * i: min(3 * i + 3, len(s))] for i in range((len(s) + 2) // 3)]
    # Reverse the cyclic shift for groups of exactly 3 characters
    groups = [(group[-1] + group[:-1]) if len(group) == 3 else group for group in groups]
    return "".join(groups)