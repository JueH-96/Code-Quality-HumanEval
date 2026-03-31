def encrypt(s):
    result = ''
    for char in s:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) - 65 + 4) % 26 + 65)
            else:
                result += chr((ord(char) - 97 + 4) % 26 + 97)
        else:
            result += char
    return result