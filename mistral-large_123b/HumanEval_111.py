def histogram(test):
    from collections import Counter

    if not test:
        return {}

    words = test.split()
    count = Counter(words)
    max_count = max(count.values())

    return {word: cnt for word, cnt in count.items() if cnt == max_count}