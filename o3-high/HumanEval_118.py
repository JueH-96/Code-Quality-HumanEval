def get_closest_vowel(word):
    """Return the closest vowel (from the right) that is surrounded by consonants."""
    vowels = set("aeiouAEIOU")
    n = len(word)
    # Need at least 3 characters to have a letter between two others
    if n < 3:
        return ""
    # Traverse from the second-to-last character down to the second character
    for i in range(n - 2, 0, -1):
        ch = word[i]
        if ch in vowels and word[i - 1] not in vowels and word[i + 1] not in vowels:
            return ch
    return ""