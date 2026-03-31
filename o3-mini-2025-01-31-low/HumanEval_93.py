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
    def shift_letter(letter):
        if letter.isupper():
            base = ord('A')
        else:
            base = ord('a')
        # advance two positions with wrap-around in 26 letters
        return chr(base + ((ord(letter) - base + 2) % 26))
    
    # Step 1: swap the case of all letters
    swapped = message.swapcase()
    
    vowels = set("aeiouAEIOU")
    encoded_chars = []
    
    # Step 2: Replace vowels with the letter that appears 2 places ahead
    for ch in swapped:
        if ch in vowels:
            encoded_chars.append(shift_letter(ch))
        else:
            encoded_chars.append(ch)
    
    return "".join(encoded_chars)