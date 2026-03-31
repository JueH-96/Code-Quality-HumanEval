def encrypt(s):
    """Encrypt the given string by shifting each alphabetical character
    forward by 4 positions in the alphabet (Caesar cipher with shift=4).
    Non-alphabetical characters are left unchanged. Case is preserved.
    """
    result = []
    for ch in s:
        if 'a' <= ch <= 'z':
            shifted = chr((ord(ch) - ord('a') + 4) % 26 + ord('a'))
            result.append(shifted)
        elif 'A' <= ch <= 'Z':
            shifted = chr((ord(ch) - ord('A') + 4) % 26 + ord('A'))
            result.append(shifted)
        else:
            result.append(ch)
    return ''.join(result)