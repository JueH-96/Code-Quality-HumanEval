def match_parens(lst):
    a, b = lst[0], lst[1]
    total_length = len(a) + len(b)
    
    if total_length % 2 != 0:
        return 'No'
    
    def is_balanced(s):
        balance = 0
        for c in s:
            if c == '(':
                balance += 1
            else:
                balance -= 1
            if balance < 0:
                return False
        return balance == 0
    
    candidate1 = a + b
    candidate2 = b + a
    
    balanced1 = is_balanced(candidate1)
    balanced2 = is_balanced(candidate2)
    
    return 'Yes' if (balanced1 or balanced2) else 'No'