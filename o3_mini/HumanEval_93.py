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
    vowels = "aeiouAEIOU"
    for ch in message:
        # Swap case
        swapped = ch.swapcase()
        # If character is a vowel (by its lowercase version)
        if swapped.lower() in "aeiou":
            if swapped.isupper():
                # For uppercase, wrap around within A-Z
                new_ord = ord('A') + ((ord(swapped) - ord('A') + 2) % 26)
            else:
                # For lowercase, wrap around within a-z
                new_ord = ord('a') + ((ord(swapped) - ord('a') + 2) % 26)
            result.append(chr(new_ord))
        else:
            result.append(swapped)
    return "".join(result)