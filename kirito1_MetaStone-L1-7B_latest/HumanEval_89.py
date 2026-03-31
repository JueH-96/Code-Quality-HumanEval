def encrypt(s):
    """Create a function encrypt that takes a string as an argument and returns it encrypted by shifting each letter four places forward in the alphabet."""
    shift = 4
    encrypted = []
    for c in s:
        if not c.isalpha():
            encrypted.append(c)
            continue
        is_upper = False
        if c.isupper():
            is_upper = True
        lower_c = c.lower()
        pos = ord(lower_c) - ord('a')
        new_pos = (pos + shift) % 26
        new_lower = chr(new_pos + ord('a'))
        if is_upper:
            encrypted.append(new_lower.upper())
        else:
            encrypted.append(new_lower)
    return ''.join(encrypted)