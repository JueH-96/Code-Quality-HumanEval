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
    stack = []
    max_depth = 0
    
    for char in string:
        if char == '[':
            stack.append(char)
            max_depth = max(max_depth, len(stack))
        elif char == ']':
            if stack:
                stack.pop()
    
    # For a valid nested structure, we need:
    # 1. All brackets to be properly matched (stack should be empty)
    # 2. Maximum depth should be at least 2 (indicating nesting)
    return len(stack) == 0 and max_depth >= 2