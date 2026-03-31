def decode_shift(s: str):
    """
    Takes as input a string encoded with the `encode_shift` function.
    Returns the decoded (original) string by shifting every character back by 5
    in the alphabet.
    """
    return "".join(chr(((ord(ch) - 5 - ord("a")) % 26) + ord("a")) for ch in s)