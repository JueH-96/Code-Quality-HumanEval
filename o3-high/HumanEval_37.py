def sort_even(l: list):
    """Return a new list where the elements at even indices are sorted,
    while the elements at odd indices remain in their original positions.

    Parameters
    ----------
    l : list
        Input list.

    Returns
    -------
    list
        List with sorted even-index elements.

    Examples
    --------
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    # Collect indices and corresponding values at even positions
    even_indices = list(range(0, len(l), 2))
    even_values = sorted(l[i] for i in even_indices)

    # Create a copy to avoid mutating the original list
    result = l.copy()

    # Place the sorted values back into their respective even indices
    for idx, val in zip(even_indices, even_values):
        result[idx] = val

    return result