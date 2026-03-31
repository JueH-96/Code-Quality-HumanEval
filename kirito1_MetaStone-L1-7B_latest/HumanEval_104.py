def unique_digits(x):
    """Given a list of positive integers x. return a sorted list of all 
    elements that hasn't any even digit.
    
    Note: Returned list should be sorted in increasing order."""
    result = []
    for num in x:
        s = str(num)
        has_even = False
        for c in s:
            d = int(c)
            if d % 2 == 0:
                has_even = True
                break
        if not has_even:
            result.append(num)
    result.sort()
    return result