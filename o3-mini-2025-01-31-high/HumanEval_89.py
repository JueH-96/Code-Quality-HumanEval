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
    shift = 2 * 2  # shift by 4 positions
    encrypted = []
    for char in s:
        if 'a' <= char <= 'z':
            # rotate within lowercase letters
            new_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            encrypted.append(new_char)
        elif 'A' <= char <= 'Z':
            # rotate within uppercase letters
            new_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            encrypted.append(new_char)
        else:
            # non-alphabetic characters remain unchanged
            encrypted.append(char)
    return ''.join(encrypted)