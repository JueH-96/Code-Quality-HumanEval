def count_nums(arr):
    """
    Write a function count_nums which takes an array of integers and returns
    the number of elements which has a sum of digits > 0.
    If a number is negative, then its first signed digit will be negative:
    e.g. -123 has signed digits -1, 2, and 3.
    >>> count_nums([]) == 0
    >>> count_nums([-1, 11, -11]) == 1
    >>> count_nums([1, 1, 2]) == 3
    """
    count = 0
    for n in arr:
        s = str(abs(n))
        if not s:
            continue
        # First digit carries the sign if negative
        total = int(s[0]) * (-1 if n < 0 else 1)
        # Add the remaining digits (always positive)
        for ch in s[1:]:
            total += int(ch)
        if total > 0:
            count += 1
    return count