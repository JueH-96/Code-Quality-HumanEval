def specialFilter(nums):
    """
    Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    def is_odd_digit(digit):
        """Check if a digit is odd"""
        return str(digit) in '13579'

    count = 0
    for num in nums:
        # Convert to string to easily access first and last digits
        str_num = str(abs(num))  # Use absolute value to handle negatives
        if len(str_num) > 1 and num > 10 and is_odd_digit(int(str_num[0])) and is_odd_digit(int(str_num[-1])):
            count += 1
    return count