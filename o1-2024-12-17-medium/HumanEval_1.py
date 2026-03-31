def separate_paren_groups(paren_string: str) -> List[str]:
    s = ''.join(paren_string.split())
    result = []
    balance = 0
    current_group = []
    for char in s:
        current_group.append(char)
        if char == '(':
            balance += 1
        else:
            balance -= 1
        if balance == 0:
            result.append(''.join(current_group))
            current_group = []
    return result