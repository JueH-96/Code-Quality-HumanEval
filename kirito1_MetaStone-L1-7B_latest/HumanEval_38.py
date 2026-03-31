def decode_cyclic(s: str) -> str:
    """
    Takes an encoded string produced by encode_cyclic and returns the original string.
    
    The process involves splitting the encoded string into triplets,
    reversing each triplet that has exactly 3 characters, then joining them back together.
    """
    groups = [s[i*3 : (i+1)*3] for i in range((len(s) + 2) // 3)]
    processed_groups = []
    
    for group in groups:
        if len(group) == 3:
            rotated_group = group[2] + group[:2]
            processed_groups.append(rotated_group)
        else:
            processed_groups.append(group)
    
    return ''.join(processed_groups)