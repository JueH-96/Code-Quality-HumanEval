def find_max(words):
    max_unique = 0
    word_with_max = ""

    for word in words:
        unique_chars = len(set(word))
        if (unique_chars > max_unique) or \
                (unique_chars == max_unique and word < word_with_max):
            max_unique = unique_chars
            word_with_max = word
    return word_with_max