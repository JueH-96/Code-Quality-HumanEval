def encrypt(s):
    result = ""
    for c in s:
        if 'a' <= c <= 'z':
            # Shift character down by two positions, wrapping around
            # when it goes past 'y'.
            result += chr((ord(c) - ord('a') + 2) % 26 + ord('a'))
        else:
            # Leave non-lowercase characters unchanged.
            result += c
    return result