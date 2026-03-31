def encode(message):
    """
    Write a function that takes a message, and encodes in such a 
    way that it swaps case of all letters, replaces all vowels in 
    the message with the letter that appears 2 places ahead of that 
    vowel in the english alphabet. 
    Assume only letters. 
    
    Examples:
    >>> encode('test')
    'TGST'
    >>> encode('This is a message')
    'tHKS KS C MGSSCGG'
    """
    vowels = 'aeiouAEIOU'
    shifted_vowels = {v: chr(ord(v) + 2) for v in vowels}
    
    encoded_message = []
    
    for char in message:
        if char.isalpha():
            if char in shifted_vowels:
                new_char = shifted_vowels[char]
            else:
                new_char = char
            encoded_message.append(new_char.swapcase())
        else:
            encoded_message.append(char)
    
    return ''.join(encoded_message)