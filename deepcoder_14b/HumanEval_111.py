def histogram(test):
    letters = test.split()
    if not letters:
        return {}
    
    freq = {}
    for letter in letters:
        if letter in freq:
            freq[letter] += 1
        else:
            freq[letter] = 1
    
    max_count = max(freq.values())
    result = {k: v for k, v in freq.items() if v == max_count}
    
    return result