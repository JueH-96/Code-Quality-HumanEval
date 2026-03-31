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
    encoded_message = ''
    
    for char in message:
        if char in vowels:
            # Find the position of the vowel (case-insensitive)
            pos = 'aeiou'.index(char.lower())
            # Replace with the letter 2 positions ahead, wrap around if necessary
            new_pos = (pos + 2) % 5
            # Preserve original case
            if char.isupper():
                encoded_message += 'AEIOU'[new_pos]
            else:
                encoded_message += 'aeiou'[new_pos]
        else:
            # Swap case for non-vowel letters
            encoded_message += char.swapcase()
    
    return encoded_message