def will_it_fly(q, w):
    '''
    Returns True if the list q is a palindrome (balanced) and the sum of its elements
    does not exceed the maximum allowed weight w. Otherwise, returns False.
    '''
    return q == q[::-1] and sum(q) <= w