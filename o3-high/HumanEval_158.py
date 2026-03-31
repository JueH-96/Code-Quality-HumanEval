def find_max(words):
    """Return the string with the highest number of unique characters.
    If several strings share the same maximum count, return the one that
    comes first in lexicographical order. If the input list is empty,
    return an empty string.
    """
    if not words:
        return ""
    
    best_word = ""
    best_unique = -1  # ensures any string will beat initial value
    
    for word in words:
        unique_count = len(set(word))
        if unique_count > best_unique or (unique_count == best_unique and word < best_word):
            best_unique = unique_count
            best_word = word
    
    return best_word