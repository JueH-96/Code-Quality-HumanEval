def is_nested(string):
    stack = []
    max_depth = 0
    for char in string:
        if char == '[':
            stack.append(char)
            if len(stack) > max_depth:
                max_depth = len(stack)
        elif char == ']':
            if stack:
                stack.pop()
            else:
                return False
    if stack:
        return False
    return max_depth > 1