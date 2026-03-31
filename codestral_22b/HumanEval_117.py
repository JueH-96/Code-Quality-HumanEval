def select_words(s, n):
    consonants = "bcdfghjklmnpqrstvwxyz"
    return [word for word in s.split() if sum(1 for char in word if char.lower() in consonants) == n]