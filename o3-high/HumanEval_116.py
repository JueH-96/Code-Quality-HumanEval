def sort_array(arr):
    """
    Sort an array of integers based on the number of '1' bits in their binary
    representation (ascending). When two numbers share the same bit-count,
    order them by their decimal value.

    Parameters
    ----------
    arr : Iterable[int]
        The input collection of integers.

    Returns
    -------
    list[int]
        The sorted list following the described criteria.
    """
    return sorted(arr, key=lambda n: (bin(n).count('1'), n))