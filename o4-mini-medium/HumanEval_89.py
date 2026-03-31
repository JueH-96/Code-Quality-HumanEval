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
    shift = 2 * 2  # shift by 4
    for ch in s:
        if 'a' <= ch <= 'z':
            # shift lowercase letters
            new_ord = (ord(ch) - ord('a') + shift) % 26 + ord('a')
            result.append(chr(new_ord))
        elif 'A' <= ch <= 'Z':
            # shift uppercase letters
            new_ord = (ord(ch) - ord('A') + shift) % 26 + ord('A')
            result.append(chr(new_ord))
        else:
            # leave other characters unchanged
            result.append(ch)
    return ''.join(result)