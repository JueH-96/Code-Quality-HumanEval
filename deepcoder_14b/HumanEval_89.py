def rotate_alphabet(s):
    rotated = []
    for c in s:
        if 'a' <= c <= 'z':
            # Handle lowercase letters
            new_char = chr((ord(c) - ord('a') + 4) % 26 + ord('a'))
            rotated.append(new_char)
        elif 'A' <= c <= 'Z':
            # Handle uppercase letters
            new_char = chr((ord(c) - ord('A') + 4) % 26 + ord('A'))
            rotated.append(new_char)
        else:
            # Non-alphabetic characters remain unchanged
            rotated.append(c)
    return ''.join(rotated)

# Example usage:
print(rotate_alphabet("hi"))          # Output: "lm"
print(rotate_alphabet("Hello, World!"))  # Output: "Lipps, Ctofq!"