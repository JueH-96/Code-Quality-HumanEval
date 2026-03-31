from collections import Counter

def search(lst):
    count = Counter(lst)
    max_valid = -1
    for num, freq in count.items():
        if freq >= num:
            if num > max_valid:
                max_valid = num
    return max_valid