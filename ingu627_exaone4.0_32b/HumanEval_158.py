def find_max(words):
    max_unique = -1
    result_word = ""
    for word in words:
        unique_chars = len(set(word))
        if unique_chars > max_unique:
            max_unique = unique_chars
            result_word = word
        elif unique_chars == max_unique:
            if word < result_word:
                result_word = word
    return result_word