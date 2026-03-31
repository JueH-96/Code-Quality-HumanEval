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
    open_count = 0
    for idx, char in enumerate(string):
        if char == '[':
            open_count += 1
            if open_count == 2:
                # Use the current index as the second '['.
                # Check if there are at least two ']' in the remainder of the string.
                if string[idx+1:].count(']') >= 2:
                    return True
                break
    return False