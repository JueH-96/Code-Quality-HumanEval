def is_nested(string):
    '''
    Create a function that takes a string as input which contains only square brackets.
    The function should return True if and only if there is a valid subsequence of brackets 
    where at least one bracket in the subsequence is nested.

    is_nested('[[]]') True
    is_nested('[]]]]]]][[[[[]') False
    is_nested('[][]') False
    is_nested('[]') False
    is_nested('[[][]]') True
    is_nested('[[]][[') True
    '''
    stack = []
    for bracket in string:
        if bracket == '[':
            stack.append(bracket)
        elif bracket == ']':
            if len(stack) > 1:  # if there's more than one opening bracket, it's nested
                return True
            if not stack:  # if there's no matching opening bracket, invalid sequence
                return False
            stack.pop()
    return False  # if the loop completes without finding a nested bracket and the stack is empty (valid sequence)