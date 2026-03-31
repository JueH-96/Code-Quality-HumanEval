def encode(message):
    """
    Write a function that takes a message, and encodes in such a way that it swaps case of all letters,
    replaces all vowels in the message with the letter that appears 2 places ahead of that vowel in the english alphabet.
    Assume only letters.

    Examples:
    >>> encode('test')
    'TGST'
    >>> encode('This is a message')
    'tHKS kS C mGSSCGG'
    """

    vowels = {'a': 'c', 'e': 'g', 'i': 'k', 'o': 'm', 'u': 'y',
              'A': 'C', 'E': 'G', 'I': 'K', 'O': 'M', 'U': 'Y'}
    encoded_message = ''

    for char in message:
        if char.isalpha():
            if char in vowels:
                char = vowels[char]
            else:
                char = char.swapcase()
        encoded_message += char

    return encoded_message