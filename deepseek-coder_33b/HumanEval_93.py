def encode(message):
    vowels = 'aeiouAEIOU'
    encoded_msg = ''
    for char in message:
        if char.isalpha():
            if char.lower() not in 'aeiou':
                encoded_char = char.swapcase()
            else:
                idx = vowels.index(char)
                encoded_char = vowels[(idx+2)%len(vowels)]
        else:
            encoded_char = char
        encoded_msg += encoded_char
    return encoded_msg