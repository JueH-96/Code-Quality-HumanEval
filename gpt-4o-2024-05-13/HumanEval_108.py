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
    def sum_of_digits(n):
        if n == 0:
            return 0
        n_str = str(n)
        if n_str[0] == '-':
            return int(n_str[0] + n_str[1]) + sum(int(d) for d in n_str[2:])
        return sum(int(d) for d in n_str)
    
    return sum(1 for num in arr if sum_of_digits(num) > 0)