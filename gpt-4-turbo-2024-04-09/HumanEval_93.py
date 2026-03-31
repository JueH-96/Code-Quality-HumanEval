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
    vowel_shift = {'a': 'c', 'e': 'g', 'i': 'k', 'o': 'q', 'u': 'w',
                   'A': 'C', 'E': 'G', 'I': 'K', 'O': 'Q', 'U': 'W'}
    encoded_message = []

    for char in message:
        if char in vowels:
            new_char = vowel_shift[char]
        else:
            new_char = char
        if new_char.islower():
            new_char = new_char.upper()
        else:
            new_char = new_char.lower()
        encoded_message.append(new_char)

    return ''.join(encoded_message)