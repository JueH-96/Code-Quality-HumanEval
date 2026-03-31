def correct_bracketing(brackets: str):
    stack = []
    
    for b in brackets:
        if b == "<":
            stack.append(b)
        else:  # assuming the input string contains only '<' and '>', no other characters
            if not stack or stack[-1] != "<":
                return False
            stack.pop()
            
    return not stack