def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the 
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    
    # Ensure x is less than or equal to y, swap if necessary
    if x > y:
        x, y = y, x
    
    # Find the largest even number in the range [x, y]
    largest_even = [i for i in range(x, y+1) if i % 2 == 0]
    
    # Return the largest even number if found, otherwise return -1
    return max(largest_even) if largest_even else -1