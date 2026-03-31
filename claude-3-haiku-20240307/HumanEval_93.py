def encode(message):
    vowels = 'aeiou'
    encoded = ''
    for char in message:
        if char.isalpha():
            if char.lower() in vowels:
                encoded += chr(ord(char.lower()) + 2)
            else:
                encoded += char.swapcase()
    return encoded