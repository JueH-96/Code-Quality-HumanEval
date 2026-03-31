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
    def sum_of_digits(num):
        return sum(int(digit) for digit in str(abs(num)))

    count = 0
    for num in arr:
        signed_digits = [int(digit) if i > 0 or num >= 0 else -int(digit) for i, digit in enumerate(str(num))]
        if sum(signed_digits) > 0:
            count += 1

    return count