def double_the_difference(lst):
    '''
    Given a list of numbers, return the sum of squares of the numbers
    in the list that are odd. Ignore numbers that are negative or not integers.
    
    double_the_difference([1, 3, 2, 0]) == 1 + 9 + 0 + 0 = 10
    double_the_difference([-1, -2, 0]) == 0
    double_the_difference([9, -2]) == 81
    double_the_difference([0]) == 0  
   
    If the input list is empty, return 0.
    '''
    total = 0
    for num in lst:
        # Check if num is an integer (or can be a float with integer value),
        # and non-negative, and odd.
        # We consider that the relevant integers are those that are of type int OR are floats with integer value.
        if (isinstance(num, int) or (isinstance(num, float) and num.is_integer())) and num >= 0:
            # Convert to int if it's float
            num_int = int(num)
            if num_int % 2 != 0:
                total += num_int ** 2
    return total