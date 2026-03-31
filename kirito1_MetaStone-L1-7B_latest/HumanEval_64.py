def vowels_count(s):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    count = 0
    for c in s:
        if c.lower() in vowels:
            count += 1
    # Check if the last character is 'y' (case-insensitive)
    if len(s) > 0 and s[-1].lower() == 'y':
        count += 1
    return count