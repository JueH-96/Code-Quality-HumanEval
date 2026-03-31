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
    pos = 0
    open1 = string.find('[', pos)
    if open1 == -1:
        return False
    open2 = string.find('[', open1 + 1)
    if open2 == -1:
        return False
    close2 = string.find(']', open2 + 1)
    if close2 == -1:
        return False
    close1 = string.find(']', close2 + 1)
    if close1 == -1:
        return False
    return True