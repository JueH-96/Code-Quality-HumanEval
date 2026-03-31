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
    def signed_digit_sum(n):
        if n == 0:
            return 0
        negative = n < 0
        n_abs = abs(n)
        digits = []
        while n_abs:
            digits.append(n_abs % 10)
            n_abs //= 10
        digits.reverse()
        if negative and digits:
            digits[0] = -digits[0]
        return sum(digits)

    count = 0
    for num in arr:
        if signed_digit_sum(num) > 0:
            count += 1
    return count