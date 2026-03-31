def histogram(test):
    if test == '':
        return {}
    else:
        words = test.split()
        word_counts = {word: words.count(word) for word in words}
        max_count = max(word_counts.values())
        most_frequent_words = {word: count for word, count in word_counts.items() if count == max_count}
    return most_frequent_words