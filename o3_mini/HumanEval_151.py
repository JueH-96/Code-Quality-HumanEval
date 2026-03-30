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
        # Check if num is an integer or a float that represents an integer
        if (isinstance(num, int) or (isinstance(num, float) and num.is_integer())) and num >= 0:
            # Convert float integers to int for modulo operation
            if int(num) % 2 != 0:
                total += int(num) ** 2
    return total