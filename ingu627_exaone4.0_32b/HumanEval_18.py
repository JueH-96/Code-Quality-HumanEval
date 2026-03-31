def how_many_times(string: str, substring: str) -> int:
    count = 0
    len_sub = len(substring)
    len_str = len(string)
    for i in range(0, len_str - len_sub + 1):
        if string[i:i+len_sub] == substring:
            count += 1
    return count