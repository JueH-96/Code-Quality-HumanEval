def select_words(s, n):
    def count_consonants(word):
        return sum((1 for ch in word if ch.lower() in 'bcdfghjklmnpqrstvwxyz'))
    
    words = s.split(' ')
    result = [word for word in words if count_consonants(word) == n]
    
    return result