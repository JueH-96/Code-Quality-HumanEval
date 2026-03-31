def is_nested(string):
    '''
    Create a function that takes a string as input which contains only square brackets.
    The function should return True if and only if there is a valid subsequence of brackets 
    where at least one bracket in the subsequence is nested.
    '''
    n = len(string)
    # suffix_closes[i] = number of ']' characters in string[i:]
    suffix_closes = [0] * (n + 1)
    for i in range(n - 1, -1, -1):
        suffix_closes[i] = suffix_closes[i + 1] + (1 if string[i] == ']' else 0)

    open_count = 0
    for i, ch in enumerate(string):
        if ch == '[':
            open_count += 1
            # We need at least two '[' so far and at least two ']' after this position
            if open_count >= 2 and suffix_closes[i + 1] >= 2:
                return True
    return False