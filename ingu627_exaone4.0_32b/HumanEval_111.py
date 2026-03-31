def histogram(test):
    letters = test.split()
    frequency = {}
    for letter in letters:
        frequency[letter] = frequency.get(letter, 0) + 1
    if not frequency:
        return {}
    max_count = max(frequency.values())
    result = {letter: count for letter, count in frequency.items() if count == max_count}
    return result