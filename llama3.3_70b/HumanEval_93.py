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
        if char.isalpha():
            # Swap case of the character
            swapped_case_char = char.swapcase()
            
            # Check if the character is a vowel
            if swapped_case_char.lower() in 'aeiou':
                # Calculate the ASCII value of the character 2 places ahead
                ascii_value = ord(swapped_case_char) + 2
                
                # If the resulting character would be after 'z' or 'Z', wrap around to the start of the alphabet
                if swapped_case_char.islower() and ascii_value > ord('z'):
                    ascii_value -= 26
                elif swapped_case_char.isupper() and ascii_value > ord('Z'):
                    ascii_value -= 26
                
                # Convert the ASCII value back to a character
                encoded_char = chr(ascii_value)
            else:
                encoded_char = swapped_case_char
            
            encoded_message += encoded_char
    
    return encoded_message