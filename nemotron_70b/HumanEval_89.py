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
    result = ""
    shift = 2 * 2  # calculate the shift value as per the problem statement
    for char in s:
        if char.isalpha():  # check if character is a letter
            ascii_offset = 97 if char.islower() else 65  # ASCII offset for 'a' or 'A'
            result += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            result += char  # if not a letter, add as is (e.g., spaces, punctuation)
    return result