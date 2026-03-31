from collections import Counter

def search(lst):
    '''
    You are given a non-empty list of positive integers. Return the greatest integer that is greater than
    zero, and has a frequency greater than or equal to the value of the integer itself.
    The frequency of an integer is the number of times it appears in the list.
    If no such a value exist, return -1.
    Examples:
        search([4, 1, 2, 2, 3, 1]) == 2
        search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3
        search([5, 5, 4, 4, 4]) == -1
    '''
    # Count the occurrences of each integer in the list
    counts = Counter(lst)
    
    # Filter out integers that satisfy the condition: frequency >= integer value
    valid_candidates = [num for num, freq in counts.items() if freq >= num]
    
    # Return the greatest such integer, or -1 if none exist
    return max(valid_candidates) if valid_candidates else -1