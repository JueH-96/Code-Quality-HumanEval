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
    vowels = 'aeiou'
    encoded_chars = []

    for ch in message:
        if ch.isalpha():
            swapped = ch.swapcase()
            if swapped.lower() in vowels:
                base = ord('A') if swapped.isupper() else ord('a')
                shifted = chr(base + (ord(swapped) - base + 2) % 26)
                encoded_chars.append(shifted)
            else:
                encoded_chars.append(swapped)
        else:
            encoded_chars.append(ch)

    return ''.join(encoded_chars)