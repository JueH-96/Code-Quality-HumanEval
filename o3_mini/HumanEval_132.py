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
    # We want to see if there exists a subsequence of four characters in order:
    # an open bracket, then another open bracket (so that one of them can wrap the inner one),
    # then a closing bracket (to close the inner open bracket),
    # and then another closing bracket (to close the outer open bracket).
    # If we can find such a sequence, that means there's at least one nested pair.
    pattern = ['[', '[', ']', ']']
    pos = 0
    for char in pattern:
        found = False
        while pos < len(string):
            if string[pos] == char:
                found = True
                pos += 1
                break
            pos += 1
        if not found:
            return False
    return True