def select_words(s, n):
    """Return a list of words from s that contain exactly n consonants."""
    vowels = set('aeiouAEIOU')
    result = []
    for word in s.split():
        consonants = sum(1 for ch in word if ch.isalpha() and ch not in vowels)
        if consonants == n:
            result.append(word)
    return result