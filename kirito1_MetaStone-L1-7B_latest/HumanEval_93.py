def encode(string):
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    encoded = []
    for c in string:
        swapped = c.swapcase()
        if swapped in vowels:
            current_pos = ord(swapped) - (ord('a') if swapped.islower() else ord('A'))
            new_pos = (current_pos + 2) % 26
            shifted_char = chr(ord('a') + new_pos) if swapped.islower() else chr(ord('A') + new_pos)
            encoded.append(shifted_char)
        else:
            encoded.append(swapped)
    return ''.join(encoded)