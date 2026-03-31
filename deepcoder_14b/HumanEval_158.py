def find_best_word(words):
    if not words:
        return ""
    
    # Calculate the maximum number of unique characters in any word
    max_unique = max(len(set(word)) for word in words)
    
    # Collect all words that have this maximum number of unique characters
    candidates = [word for word in words if len(set(word)) == max_unique]
    
    # Return the lexicographically smallest word among the candidates
    return min(candidates)

# Example usage:
words = ["abc", "def"]
print(find_best_word(words))  # Output: 'abc'