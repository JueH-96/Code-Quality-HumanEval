def is_nested(string):
    stack = []
    for char in string:
        if char == '[':
            stack.append(char)
        elif char == ']' and stack:
            stack.pop()
        else:
            return False
    return len(stack) == 0 and any(c == '[' for c in string[1:-1]) if string else False