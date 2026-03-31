from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    result = []  # This will store the separated groups of parentheses.
    stack = []   # This is a helper stack to balance the parentheses.
    group = ''   # This will hold the current group of parentheses.

    for paren in paren_string:
        if paren == '(':
            stack.append(paren)
        elif paren == ')':
            stack.pop()

        if not group and stack:  # If this is the start of a new group, add the opening parenthesis to the group.
            group += paren
        elif group and not stack:  # If this is the end of a group, append the group to the result list and reset it.
            group += paren
            result.append(group)
            group = ''
        else:  # Otherwise, just add the parenthesis to the current group.
            group += paren
    return result