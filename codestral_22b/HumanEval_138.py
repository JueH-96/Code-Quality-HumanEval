def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    # The sum of four even numbers would always be a multiple of 8. So, if n is not a multiple of 8, return False.
    # Also, since we're looking for positive even numbers, n should be greater than or equal to 8.
    if n < 8 or n % 8 != 0:
        return False
    else:
        return True