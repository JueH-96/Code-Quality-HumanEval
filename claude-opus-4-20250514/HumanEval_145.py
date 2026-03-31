def order_by_points(nums):
    """
    Write a function which sorts the given list of integers
    in ascending order according to the sum of their digits.
    Note: if there are several items with similar sum of their digits,
    order them based on their index in original list.

    For example:
    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points([]) == []
    """
    def sum_of_digits(n):
        # Handle negative numbers by taking absolute value for digit sum
        # but keeping track of the sign
        if n < 0:
            return sum(int(digit) for digit in str(-n)) * -1 + int(str(n)[0] == '-') * int(str(-n)[0])
        else:
            return sum(int(digit) for digit in str(n))
    
    # Create list of tuples (original_index, value, sum_of_digits)
    indexed_nums = [(i, num, sum_of_digits(num)) for i, num in enumerate(nums)]
    
    # Sort by sum of digits first, then by original index
    indexed_nums.sort(key=lambda x: (x[2], x[0]))
    
    # Extract just the values
    return [x[1] for x in indexed_nums]