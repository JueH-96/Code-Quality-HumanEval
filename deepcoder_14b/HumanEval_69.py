from collections import Counter

def search(lst):
    counts = Counter(lst)
    candidates = []
    for num in counts:
        if counts[num] >= num:
            candidates.append(num)
    return max(candidates) if candidates else -1