def encode(message):
    vowels = "aeiouAEIOU"
    replacements = {
        'a': 'c', 'e': 'g', 'i': 'k', 'o': 'q', 'u': 'w',
        'A': 'C', 'E': 'G', 'I': 'K', 'O': 'Q', 'U': 'W'
    }
    encoded_message = []

    for char in message:
        if char.islower():
            if char in vowels:
                encoded_message.append(replacements[char])
            else:
                encoded_message.append(char.upper())
        elif char.isupper():
            if char in vowels:
                encoded_message.append(replacements[char])
            else:
                encoded_message.append(char.lower())

    return ''.join(encoded_message)