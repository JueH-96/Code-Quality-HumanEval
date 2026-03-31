def match_parens(lst):
    left = lst[0].count('(')
    right = lst[1].count(')')
    if left >= right:
        return 'Yes'
    else:
        return 'No'