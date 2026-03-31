def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # Remove spaces
    paren_string = paren_string.replace(' ', '')
    
    groups = []
    current_group = []
    depth = 0
    
    for char in paren_string:
        if char == '(':
            current_group.append(char)
            depth += 1
        elif char == ')':
            current_group.append(char)
            depth -= 1
            
            # When depth reaches 0, we've completed a group
            if depth == 0:
                groups.append(''.join(current_group))
                current_group = []
    
    return groups