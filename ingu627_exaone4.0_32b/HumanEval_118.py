def get_closest_vowel(word):
    vowels = "aeiouAEIOU"
    n = len(word)
    # Traverse from right to left, starting from the second last character (since last character is excluded)
    for i in range(n-2, 0, -1):
        if word[i] in vowels:
            # Check the left and right neighbors are consonants (not vowels)
            left_char = word[i-1]
            right_char = word[i+1]
            if left_char not in vowels and right_char not in vowels:
                return word[i]
    return ""