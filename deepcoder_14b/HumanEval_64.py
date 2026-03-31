def vowels_count(s):
    count = 0
    for char in s:
        lower_char = char.lower()
        if lower_char in {'a', 'e', 'i', 'o', 'u'}:
            count += 1
    # Check if the last character is 'y' or 'Y'
    if s:  # Ensure the string is not empty to avoid index error
        last_char = s[-1].lower()
        if last_char == 'y':
            count += 1
    return count