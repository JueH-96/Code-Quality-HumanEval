def flip_case(string: str) -> str:
    flipped = ''
    for char in string:
        if char.islower():
            flipped += char.upper()
        else:
            flipped += char.lower()
    return flipped