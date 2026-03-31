def remove_vowels(text):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    result = []
    for c in text:
        if c.lower() not in vowels:
            result.append(c)
    return ''.join(result)