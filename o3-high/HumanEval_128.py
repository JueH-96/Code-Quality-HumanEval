def prod_signs(arr):
    """
    Returns the sum of magnitudes of the integers in `arr` multiplied by the
    product of their signs (1 for positive, -1 for negative, 0 for zero).

    Parameters
    ----------
    arr : list[int]
        List of integers.

    Returns
    -------
    int or None
        Calculated value or None if `arr` is empty.

    Examples
    --------
    >>> prod_signs([1, 2, 2, -4])
    -9
    >>> prod_signs([0, 1])
    0
    >>> prod_signs([])
    """
    if not arr:  # Handle empty list
        return None

    sum_mag = 0
    sign_product = 1

    for num in arr:
        sum_mag += abs(num)
        if num == 0:
            sign = 0
        elif num > 0:
            sign = 1
        else:
            sign = -1
        sign_product *= sign

    return sign_product * sum_mag