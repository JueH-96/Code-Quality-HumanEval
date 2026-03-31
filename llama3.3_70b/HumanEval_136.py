def largest_smallest_integers(lst):
    '''
    Create a function that returns a tuple (a, b), where 'a' is 
    the largest of negative integers, and 'b' is the smallest 
    of positive integers in a list.
    If there is no negative or positive integers, return them as None.

    Examples:
    largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (None, 1)
    largest_smallest_integers([]) == (None, None)
    largest_smallest_integers([0]) == (None, None)
    '''
    negative_numbers = [num for num in lst if num < 0]
    positive_numbers = [num for num in lst if num > 0]

    a = max(negative_numbers) if negative_numbers else None
    b = min(positive_numbers) if positive_numbers else None

    return (a, b)