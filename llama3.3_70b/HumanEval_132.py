def is_nested(string):
    stack = []
    for char in string:
        if char == '[':
            stack.append(char)
        elif char == ']':
            if len(stack) > 1:  # if there are more than one opening bracket, it means the current closing bracket is nested
                return True
            if not stack:  # if there are no opening brackets to match with the current closing bracket
                return False
            stack.pop()
    return False