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
    count_open = 0
    found_inner_closed = False
    for ch in string:
        if ch == '[':
            count_open += 1
        else:  # ch == ']'
            if found_inner_closed:
                return True
            if count_open >= 2:
                found_inner_closed = True
    return False