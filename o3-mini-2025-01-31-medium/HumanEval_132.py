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
    # To have a nested valid subsequence, we need to find indices i, j, k, l where:
    # i < j < k < l, string[i]=='[', string[j]=='[', string[k]==']', string[l]==']'
    # This corresponds to the subsequence "[ [ ] ]"
    #
    # The idea is to iterate over every occurrence of '[' (except the first)
    # and if we can find at least two closing brackets ']' after that position,
    # then we can form the subsequence.
    
    # Collect the indices of all opening brackets.
    left_indices = [i for i, ch in enumerate(string) if ch == '[']
    
    # We need at least two opening brackets to be able to nest.
    if len(left_indices) < 2:
        return False

    # For each occurrence of '[' starting from the second one (as inner bracket),
    # check if there are at least two closing brackets after its position.
    for idx in left_indices[1:]:
        # Count the number of ']' that come after this '[' in the string.
        if string[idx+1:].count(']') >= 2:
            return True

    return False