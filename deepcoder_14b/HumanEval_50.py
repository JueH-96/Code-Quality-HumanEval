def decode_shift(s):
    return ''.join([chr(((ord(c) - ord('a') - 5) % 26) + ord('a')) for c in s])