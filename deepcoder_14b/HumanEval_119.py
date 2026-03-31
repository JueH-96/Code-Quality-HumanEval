def match_parens(lst):
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

    option1 = lst[0] + lst[1]
    option2 = lst[1] + lst[0]

    return 'Yes' if is_balanced(option1) or is_balanced(option2) else 'No'

# Example usage:
# print(match_parens(['(()', ')']))  # Should output 'Yes'