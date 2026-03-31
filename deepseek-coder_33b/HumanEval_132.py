def is_nested(string):
    stack = []
    for bracket in string:
        if bracket == '[':
            stack.append(bracket)
        elif len(stack) > 0 and bracket == ']':
            return True
        else:
            return False
    return False