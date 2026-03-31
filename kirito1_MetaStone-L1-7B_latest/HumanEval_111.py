from collections import Counter

def histogram(test):
    """Given a string representing a space separated lowercase letters, return a dictionary
    of the letter with the most repetition and containing the corresponding count.
    If several letters have the same occurrence, return all of them."""
    words = test.split()
    if not words:
        return {}
    counts = Counter(words)
    max_count = max(counts.values())
    result = {letter: cnt for letter, cnt in counts.items() if cnt == max_count}
    return result