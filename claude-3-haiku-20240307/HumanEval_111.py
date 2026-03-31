def histogram(test):
    if not test:
        return {}
    
    count = {}
    for char in test.split():
        count[char] = count.get(char, 0) + 1
    
    max_count = max(count.values())
    return {k: v for k, v in count.items() if v == max_count}