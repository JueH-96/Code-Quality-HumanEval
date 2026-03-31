def count_upper(s):
    count = 0
    for index, char in enumerate(s):
        if index % 2 == 0 and char in {'A', 'E', 'I', 'O', 'U'}:
            count += 1
    return count