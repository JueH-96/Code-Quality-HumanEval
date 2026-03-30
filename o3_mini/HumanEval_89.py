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
    shift = 2 * 2  # equals 4
    result = []
    for char in s:
        if char.isalpha() and char.islower():
            new_char_ord = (ord(char) - ord('a') + shift) % 26 + ord('a')
            result.append(chr(new_char_ord))
        elif char.isalpha() and char.isupper():
            new_char_ord = (ord(char) - ord('A') + shift) % 26 + ord('A')
            result.append(chr(new_char_ord))
        else:
            result.append(char)
    return ''.join(result)