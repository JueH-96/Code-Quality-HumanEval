from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    paren_string = paren_string.replace(' ', '')
    stack = []
    result = []
    group = ''
    for char in paren_string:
        if char == '(':
            if group:
                stack.append(group)
                group = ''
            group += char
        elif char == ')':
            group += char
            if stack:
                group = stack.pop() + group
            result.append(group)
            group = ''
    return result