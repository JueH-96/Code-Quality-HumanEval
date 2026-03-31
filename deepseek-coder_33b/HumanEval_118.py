def get_closest_vowel(word):
    vowels = set('AEIOUaeiou')
    for i in range(len(word) - 1, 0, -1):
        if word[i-1] not in vowels and word[i] in vowels:
            return word[i]
    return ""