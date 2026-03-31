def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    number of unique characters. If multiple strings have maximum number
    of unique characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == "aaaaaaa"
    """
    if not words:
        return ""
    max_count = -1
    result = None
    for word in words:
        uniq_count = len(set(word))
        if uniq_count > max_count:
            max_count = uniq_count
            result = word
        elif uniq_count == max_count and word < result:
            result = word
    return result