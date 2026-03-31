def how_many_times(string: str, substring: str) -> int:
    count = start = 0
    while start < len(string):
        pos = string.find(substring, start)  # find position of substring in the string
        if pos != -1:  # if found
            start = pos + 1  # move to next char after finding substring
            count += 1  # increment count
        else:  
            break  # break loop when no substring is found
    return count