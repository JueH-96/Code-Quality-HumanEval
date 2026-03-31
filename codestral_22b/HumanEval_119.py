def match_parens(lst):
    open_count = [s.count('(') for s in lst]
    close_count = [s.count(')') for s in lst]

    # If the sum of open and close parentheses is not equal, it's impossible to make a good string
    if sum(open_count + close_count) % 2 != 0:
        return 'No'

    # Make the first string with more closing parentheses as the second string in concatenation
    if open_count[1] > close_count[1]:
        lst.reverse()

    # If the number of opening parentheses in the first string is greater than or equal to the number of closing parentheses in the second string, it's possible to make a good string
    if open_count[0] >= close_count[1]:
        return 'Yes'

    return 'No'