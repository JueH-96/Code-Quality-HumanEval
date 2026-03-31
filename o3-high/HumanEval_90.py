def next_smallest(lst):
    """
    Returns the 2nd smallest distinct element in the list.
    If fewer than two distinct elements exist, returns None.
    """
    distinct_numbers = set(lst)
    if len(distinct_numbers) < 2:
        return None

    smallest = second_smallest = None
    for num in distinct_numbers:
        if smallest is None or num < smallest:
            second_smallest, smallest = smallest, num
        elif second_smallest is None or smallest < num < second_smallest:
            second_smallest = num

    return second_smallest