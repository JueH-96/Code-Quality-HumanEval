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

    s1, s2 = lst
    return 'Yes' if is_good(s1 + s2) or is_good(s2 + s1) else 'No'