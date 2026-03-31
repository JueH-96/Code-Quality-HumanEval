def is_rotation_substring(a, b):
    # Handle the case where both strings are empty
    if not a and not b:
        return True
    # If b is an empty string, it's a substring of any string a
    if not b:
        return True
    len_a = len(a)
    len_b = len(b)
    # If a is shorter than b, no rotation can be a substring
    if len_a < len_b:
        return False
    # Generate all possible rotations of b
    rotations = [b[i:] + b[:i] for i in range(len_b)]
    # Check each rotation against the string a
    for r in rotations:
        if r in a:
            return True
    return False