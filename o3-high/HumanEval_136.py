def largest_smallest_integers(lst):
    '''
    Returns a tuple (largest_negative, smallest_positive) from the given list.

    largest_negative : the negative integer with the greatest value (closest to 0)
    smallest_positive: the positive integer with the smallest value

    If the list lacks negative or positive integers, their place in the tuple is None.
    '''
    largest_negative = None
    smallest_positive = None

    for item in lst:
        # Ignore non-numeric or non-integer values
        if not isinstance(item, int):
            continue

        if item < 0:
            if largest_negative is None or item > largest_negative:
                largest_negative = item
        elif item > 0:
            if smallest_positive is None or item < smallest_positive:
                smallest_positive = item

    return (largest_negative, smallest_positive)