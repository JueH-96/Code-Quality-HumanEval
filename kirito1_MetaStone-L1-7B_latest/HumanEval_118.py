def get_closest_vowel(word):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    for i in reversed(range(1, len(word) - 1)):
        if word[i].lower() in vowels:
            prev_char = word[i-1].lower()
            next_char = word[i+1].lower()
            if (prev_char not in vowels) and (next_char not in vowels):
                return word[i]
    return ""