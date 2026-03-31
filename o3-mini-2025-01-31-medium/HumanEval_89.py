def encrypt(s):
    """Create a function encrypt that takes a string as an argument and
    returns a string encrypted with the alphabet being rotated. 
    The alphabet should be rotated in a manner such that the letters 
    shift down by two multiplied to two places.
    For example:
    encrypt('hi') returns 'lm'
    encrypt('asdfghjkl') returns 'ewhjklnop'
    encrypt('gf') returns 'kj'
    encrypt('et') returns 'ix'
    """
    result = []
    shift = 2 * 2  # 2 multiplied by 2 yields shift of 4
    for c in s:
        if c.isalpha():
            # Determine base (for uppercase or lowercase)
            base = ord('A') if c.isupper() else ord('a')
            # Rotate character within the alphabet
            new_char = chr((ord(c) - base + shift) % 26 + base)
            result.append(new_char)
        else:
            # For non alphabetic characters, just use them as is.
            result.append(c)
    return ''.join(result)