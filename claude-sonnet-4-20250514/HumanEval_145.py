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
    def digit_sum(n):
        if n == 0:
            return 0
        
        # Handle negative numbers
        if n < 0:
            # For negative numbers, subtract the first digit and add the rest
            str_n = str(abs(n))
            return -int(str_n[0]) + sum(int(digit) for digit in str_n[1:])
        else:
            # For positive numbers, sum all digits
            return sum(int(digit) for digit in str(n))
    
    # Create list of (value, original_index, digit_sum) tuples
    indexed_nums = [(num, i, digit_sum(num)) for i, num in enumerate(nums)]
    
    # Sort by digit sum first, then by original index
    indexed_nums.sort(key=lambda x: (x[2], x[1]))
    
    # Return just the values
    return [x[0] for x in indexed_nums]