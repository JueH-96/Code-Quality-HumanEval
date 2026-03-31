def encode(message):
    vowels = 'aeiouAEIOU'
    alphabet_lower = 'abcdefghijklmnopqrstuvwxyzabcd'
    alphabet_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCD'
    
    encoded = ''
    for char in message:
        if char.isalpha():
            if char in vowels:
                # find the next vowel
                ix = alphabet_lower.index(char) + 2 
                if char.isupper():
                    encoded += alphabet_upper[ix]
                else:
                    encoded += alphabet_lower[ix]
            elif char.islower():
                # swap to upper case and find the next vowel
                char = char.upper()
                ix = alphabet_lower.index(char) + 2 
                if char in vowels:
                    encoded += alphabet_upper[ix]
                else:
                    encoded += alphabet_lower[ix]
            elif char.isupper():
                # swap to lower case and find the next vowel
                char = char.lower()
                ix = alphabet_lower.index(char) + 2 
                if char in vowels:
                    encoded += alphabet_upper[ix]
                else:
                    encoded += alphabet_lower[ix]
        else:
            # keep non-letter characters as they are
            encoded += char
    return encoded