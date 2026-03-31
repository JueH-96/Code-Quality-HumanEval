def next_smallest(lst):
    s = sorted(lst)
    if len(s) < 2:
        return None
    seen = set()
    unique_sorted = []
    for num in s:
        if num not in seen:
            seen.add(num)
            unique_sorted.append(num)
    if len(unique_sorted) >= 2:
        return unique_sorted[1]
    else:
        return None