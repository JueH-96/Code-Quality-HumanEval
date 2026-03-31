def search(lst):
    from collections import Counter
    counts = Counter(lst)
    max_valid = -1
    for num, freq in counts.items():
        if num > 0 and freq >= num:
            max_valid = max(max_valid, num)
    return max_valid