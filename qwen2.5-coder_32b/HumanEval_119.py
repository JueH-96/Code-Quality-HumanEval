def match_parens(lst):
    def is_good(s):
        balance = 0
        for char in s:
            if char == '(':
                balance += 1
            else:
                balance -= 1
            if balance < 0:
                return False
        return balance == 0

    first_order = lst[0] + lst[1]
    second_order = lst[1] + lst[0]

    if is_good(first_order) or is_good(second_order):
        return 'Yes'
    else:
        return 'No'