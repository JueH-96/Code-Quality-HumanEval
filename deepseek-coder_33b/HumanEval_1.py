def separate_paren_groups(paren_string):
    paren_string = paren_string.replace(' ', '')
    result, stack, curr = [], [], ''

    for char in paren_string:
        if char == '(':
            if len(curr) > 0 and not stack:  # start a new group
                result.append(curr)
                curr = ''
                
            stack.append(char)
            
        elif char == ')' and stack[-1] == '(':
            stack.pop()
        
        curr += char
    
    if curr:  # add remaining group, if any
        result.append(curr)
    
    return result