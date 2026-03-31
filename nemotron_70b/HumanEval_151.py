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
    # Filter out non-integer and negative numbers, then filter odd numbers
    odd_numbers = [num for num in lst if isinstance(num, int) and num >= 0 and num % 2 != 0]
    
    # Calculate sum of squares of the odd numbers (no need to "double" as per function name)
    result = sum([num ** 2 for num in odd_numbers])
    
    return result