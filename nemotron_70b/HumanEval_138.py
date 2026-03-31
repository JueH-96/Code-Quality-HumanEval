def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    if n < 8:  # smallest possible sum of 4 even numbers is 2+2+2+2 = 8
        return False
    
    for a in range(2, n//4 + 1, 2):  # loop through possible first even number
        for b in range(a, (n-a)//3 + 1, 2):  # loop through possible second even number
            for c in range(b, (n-a-b)//2 + 1, 2):  # loop through possible third even number
                d = n - a - b - c
                if d >= c and d % 2 == 0:  # check if fourth number is even and not less than third
                    return True
    return False