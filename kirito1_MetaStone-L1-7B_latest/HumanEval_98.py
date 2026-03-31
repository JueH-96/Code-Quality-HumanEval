def count_upper(s):
    count = 0
    for i, c in enumerate(s):
        if i % 2 == 0 and c in {'A', 'E', 'I', 'O', 'U'}:
            count += 1
    return count