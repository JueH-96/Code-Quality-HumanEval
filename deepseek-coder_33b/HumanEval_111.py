from collections import Counter

def histogram(test):
    count = Counter(test.split())
    max_count = max(count.values(), default=0)
    return {k: v for k, v in count.items() if v == max_count}