def is_nested(string):
    '''
    Create a function that takes a string as input which contains only square brackets.
    The function should return True if and only if there is a valid subsequence of brackets 
    where at least one bracket in the subsequence is nested.

    is_nested('[[]]') ➞ True
    is_nested('[]]]]]]][[[[[]') ➞ False
    is_nested('[][]') ➞ False
    is_nested('[]') ➞ False
    is_nested('[[][]]') ➞ True
    is_nested('[[]][[') ➞ True
    '''
    n = len(string)
    # We need to check if there exist indices i < j < k < l such that:
    # string[i] = '[', string[j] = '[', string[k] = ']', string[l] = ']'
    # because that sequence implies a nested bracket structure.
    for i in range(n):
        if string[i] != '[':
            continue
        for j in range(i+1, n):
            if string[j] != '[':
                continue
            # Found two '[' in order, now look for two ']' after j.
            first_close = -1
            for k in range(j+1, n):
                if string[k] == ']':
                    first_close = k
                    break
            if first_close == -1:
                continue
            second_close = -1
            for l in range(first_close+1, n):
                if string[l] == ']':
                    second_close = l
                    break
            if second_close != -1:
                return True
    return False