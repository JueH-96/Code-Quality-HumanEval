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
    vowels = "aeiouAEIOU"
    encoded_chars = []
    for char in message:
        # Swap the case of the character.
        swapped = char.swapcase()
        # If the swapped character is a vowel, replace it with the letter 2 positions ahead.
        if swapped in vowels:
            swapped = chr(ord(swapped) + 2)
        encoded_chars.append(swapped)
    return "".join(encoded_chars)