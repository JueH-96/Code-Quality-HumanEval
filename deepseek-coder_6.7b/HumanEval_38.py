def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.
    """
    # split string to groups. Each of length 3.
    groups = [s[i:min((i + 3), len(s))] for i in range(0, len(s), 3)]
    
    # cycle elements in each group. Unless group has fewer elements than 3.
    groups = [groups[i][1:] + groups[i][0] if len(groups[i]) == 3 else groups[i] for i in range(len(groups))]
    
    return "".join(groups)

def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    # split string to groups. Each of length 3.
    groups = [s[i:min((i + 3), len(s))] for i in range(0, len(s), 3)]
    
    # reverse cycle operation in each group. Unless group has fewer elements than 3.
    groups = [groups[i][-1] + groups[i][:-1] if len(groups[i]) == 3 else groups[i] for i in range(len(groups))]
    
    return "".join(groups)