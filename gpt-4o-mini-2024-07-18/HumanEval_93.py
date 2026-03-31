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
    encoded_message = []

    for char in message:
        if char.isalpha():
            # Swap case
            if char in vowels:
                # Replace vowel with the letter 2 places ahead
                if char.islower():
                    new_char = chr(((ord(char) - ord('a') + 2) % 26) + ord('a'))
                else:
                    new_char = chr(((ord(char) - ord('A') + 2) % 26) + ord('A'))
                encoded_message.append(new_char)
            else:
                encoded_message.append(char.swapcase())
        else:
            encoded_message.append(char)

    return ''.join(encoded_message)