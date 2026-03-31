def get_closest_vowel(word):
    vowels = "AEIOUaeiou"
    for i in range(len(word)-1, -1, -1):
        if word[i] not in vowels and i+1 < len(word) and word[i+1] in vowels:
            return word[i+1]
        elif i-1 >= 0 and word[i] in vowels and word[i-1] not in vowels:
            return word[i]
    return ""