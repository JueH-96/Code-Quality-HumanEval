def encrypt(s):
    def shift_char(c, shift):
        if c.isalpha():
            base = ord('a') if c.islower() else ord('A')
            return chr((ord(c) - base + shift) % 26 + base)
        return c

    shift = 4
    return ''.join(shift_char(c, shift) for c in s)