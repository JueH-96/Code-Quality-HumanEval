def unique_digits(x):
    """Given a list of positive integers x, return a sorted list of all 
    elements that don't contain any even digit.

    Note: Returned list is sorted in increasing order.
    """
    return sorted([n for n in x if all(int(d) % 2 == 1 for d in str(n))])