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
    result = []
    for char in message:
        if char.isalpha():
            swapped = char.swapcase()
            if swapped.lower() in 'aeiou':
                if swapped.isupper():
                    base = ord('A')
                    new_char = chr((ord(swapped) - base + 2) % 26 + base)
                else:
                    base = ord('a')
                    new_char = chr((ord(swapped) - base + 2) % 26 + base)
            else:
                new_char = swapped
        else:
            new_char = char
        result.append(new_char)
    return ''.join(result)