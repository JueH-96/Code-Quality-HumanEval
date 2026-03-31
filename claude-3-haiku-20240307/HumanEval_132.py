def is_nested(string):
    stack = []
    for char in string:
        if char == '[':
            stack.append(char)
        elif char == ']':
            if len(stack) > 1 and stack[-1] == '[' and stack[-2] == '[':
                return True
            elif len(stack) > 0:
                stack.pop()
    return False