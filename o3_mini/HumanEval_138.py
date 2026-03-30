def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    # The smallest sum of 4 positive even numbers (each at least 2) is 2+2+2+2 = 8.
    # In general, any even number n >= 8 can be written as such a sum.
    return n >= 8 and n % 2 == 0