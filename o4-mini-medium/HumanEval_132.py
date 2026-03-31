def is_nested(string):
    '''
    Create a function that takes a string as input which contains only square brackets.
    The function should return True if and only if there is a valid subsequence of brackets 
    where at least one bracket in the subsequence is nested.

    is_nested('[[]]') ➞ True
    is_nested('[]]]]]]][[[[[]') ➞ False
    is_nested('[][]') ➞ False
    is_nested('[]') ➞ False
    is_nested('[[][]]') ➞ True
    is_nested('[[]][[') ➞ True
    '''
    total_closes = string.count(']')
    closes_seen = 0
    opens_count = 0
    for ch in string:
        if ch == ']':
            closes_seen += 1
        else:  # ch == '['
            opens_count += 1
            if opens_count >= 2 and (total_closes - closes_seen) >= 2:
                return True
    return False