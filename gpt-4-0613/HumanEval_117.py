def select_words(s, n):
    vowels = 'aeiouAEIOU'
    words = s.split()
    result = []
    for word in words:
        consonants = sum(1 for char in word if char not in vowels)
        if consonants == n:
            result.append(word)
    return result