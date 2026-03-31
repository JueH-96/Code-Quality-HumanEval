def search(lst):
    from collections import Counter
    cnt = Counter(lst)
    for k, v in sorted(cnt.items(), reverse=True):
        if k <= v: return k
    return -1