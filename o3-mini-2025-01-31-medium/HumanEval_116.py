def sort_array(arr):
    """
    In this Kata, you have to sort an array of non-negative integers according to
    number of ones in their binary representation in ascending order.
    For similar number of ones, sort based on decimal value.

    It must be implemented like this:
    >>> sort_array([1, 5, 2, 3, 4]) == [1, 2, 4, 3, 5]
    >>> sort_array([-2, -3, -4, -5, -6]) == [-6, -5, -4, -3, -2]
    >>> sort_array([1, 0, 2, 3, 4]) == [0, 1, 2, 4, 3]
    """
    # For non-negative integers, we sort using the tuple (number of ones in binary, value)
    # This is the standard way to solve the "Sort by Bit Count" kata.
    #
    # In case the array contains any negative numbers, we fall back to simple ascending sort.
    if all(x >= 0 for x in arr):
        return sorted(arr, key=lambda x: (bin(x).count('1'), x))
    else:
        return sorted(arr)