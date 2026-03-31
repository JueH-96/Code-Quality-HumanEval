def select_words(s, n):
    words = s.split()
    result = []
    for word in words:
        consonants = sum(1 for c in word if c.isalpha() and c.lower() not in 'aeiou')
        if consonants == n:
            result.append(word)
    return result