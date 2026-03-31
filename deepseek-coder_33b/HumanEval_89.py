def encrypt(s):
    encrypted_string = ""
    for char in s:
        if char.isalpha():
            stayInAlphabet = ord(char) + (2*2) # Rotate two places times 2
            if char.isupper():
                if stayInAlphabet > ord('Z'):
                    stayInAlphabet -= 26
                finalLetter = chr(stayInAlphabet)
            elif char.islower():
                if stayInAlphabet > ord('z'):
                    stayInAlphabet -= 26
                finalLetter = chr(stayInAlphabet)
            encrypted_string += finalLetter
    return encrypted_string