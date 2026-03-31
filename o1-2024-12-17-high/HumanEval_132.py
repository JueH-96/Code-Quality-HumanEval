def is_nested(string):
    '''
    Create a function that takes a string as input which contains only square brackets.
    The function should return True if and only if there is a valid substring of brackets 
    where at least one bracket in the substring is nested.
    '''
    n = len(string)
    for i in range(n):
        stack = 0
        max_depth = 0
        for j in range(i, n):
            if string[j] == '[':
                stack += 1
                max_depth = max(max_depth, stack)
            else:  # string[j] == ']'
                if stack == 0:
                    break
                stack -= 1
            if stack == 0 and max_depth >= 2:
                return True
    return False