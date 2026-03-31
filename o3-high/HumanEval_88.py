def sort_array(array):
    """
    Given an array of non-negative integers, return a copy of the given array after sorting.
    Sort the array in ascending order if the sum of the first and last element is odd,
    or sort it in descending order if the sum is even.

    Note:
    * The original array must remain unchanged.

    Examples:
    * sort_array([]) => []
    * sort_array([5]) => [5]
    * sort_array([2, 4, 3, 0, 1, 5]) => [0, 1, 2, 3, 4, 5]
    * sort_array([2, 4, 3, 0, 1, 5, 6]) => [6, 5, 4, 3, 2, 1, 0]
    """
    # Return a copy for empty or single-element arrays (sorting direction is irrelevant)
    if len(array) <= 1:
        return array[:]

    # Determine sorting order based on the parity of the sum of first and last elements
    reverse_order = (array[0] + array[-1]) % 2 == 0  # True => descending, False => ascending
    return sorted(array, reverse=reverse_order)