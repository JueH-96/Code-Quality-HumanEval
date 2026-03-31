def encode(s):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    result = []
    
    for c in s:
        if c.lower() in vowels:
            # Shift the vowel by two positions
            if c.islower():
                shifted_char = chr((ord(c) - ord('a') + 2) % 26 + ord('a'))
            else:
                shifted_char = chr((ord(c) - ord('A') + 2) % 26 + ord('A'))
            # Swap the case of the shifted character
            result.append(shifted_char.swapcase())
        else:
            # Swap the case for non-vowel characters
            result.append(c.swapcase())
    
    return ''.join(result)

# Example usage:
print(encode("Hello World!"))  # Output: "hGLLQ wQLRD!"