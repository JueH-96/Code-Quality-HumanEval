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
    vowels = set('aeiou')
    result = []
    for c in message:
        if c.isalpha():
            swapped = c.swapcase()
            if swapped.lower() in vowels:
                if swapped.isupper():
                    base = ord('A')
                else:
                    base = ord('a')
                pos = ord(swapped) - base
                new_char = chr((pos + 2) % 26 + base)
                result.append(new_char)
            else:
                result.append(swapped)
        else:
            result.append(c)
    return ''.join(result)