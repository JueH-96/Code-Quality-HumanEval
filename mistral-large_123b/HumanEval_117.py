def select_words(s, n):
    vowels = "aeiouAEIOU"
    def count_consonants(word):
        return sum(1 for char in word if char not in vowels)

    result = [word for word in s.split() if count_consonants(word) == n]
    return result