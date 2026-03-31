def histogram(test):
    if not test:
        return {}
    
    from collections import Counter
    
    letters = test.split()
    count = Counter(letters)
    max_count = max(count.values())
    
    return {letter: cnt for letter, cnt in count.items() if cnt == max_count}