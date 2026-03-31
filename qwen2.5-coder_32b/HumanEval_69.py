def search(lst):
    from collections import Counter
    count = Counter(lst)
    result = -1
    for num, freq in count.items():
        if num <= freq and num > result:
            result = num
    return result