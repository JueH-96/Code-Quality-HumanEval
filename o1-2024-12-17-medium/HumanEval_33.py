def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    indices_div_by_3 = [i for i in range(len(l)) if i % 3 == 0]
    values_div_by_3 = [l[i] for i in indices_div_by_3]
    values_div_by_3.sort()
    result = l[:]
    for idx, val in zip(indices_div_by_3, values_div_by_3):
        result[idx] = val
    return result