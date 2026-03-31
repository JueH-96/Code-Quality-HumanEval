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
    swapped = message.swapcase()
    vowel_map = {
        'A': 'C', 'E': 'G', 'I': 'K', 'O': 'Q', 'U': 'W',
        'a': 'c', 'e': 'g', 'i': 'k', 'o': 'q', 'u': 'w'
    }
    result = []
    for ch in swapped:
        if ch in vowel_map:
            result.append(vowel_map[ch])
        else:
            result.append(ch)
    return ''.join(result)