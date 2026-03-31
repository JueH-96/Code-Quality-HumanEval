def select_words(s, n):
    """Given a string s and a natural number n, return a list of all words from
    s that contain exactly n consonants, in order they appear in s. If the string
    s is empty then the function returns an empty list.
    """
    vowels = set("aeiouAEIOU")
    words = s.split()
    result = []
    
    for word in words:
        consonant_count = sum(1 for char in word if char not in vowels and char.isalpha())
        if consonant_count == n:
            result.append(word)
    
    return result