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
    first = string.find('[')
    if first == -1:
        return False
    second = string.find('[', first + 1)
    if second == -1:
        return False
    third = string.find(']', second + 1)
    if third == -1:
        return False
    fourth = string.find(']', third + 1)
    return fourth != -1