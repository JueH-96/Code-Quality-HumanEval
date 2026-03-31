def starts_one_ends(n):
    if n < 2:   # If n is less than 2, there are no numbers that meet the criteria so return 0.
        return 0
    
    count = 0
    for i in range(10**(n-1), 10**n):  # This loop checks each n digit number
        if str(i)[0] == '1' or str(i)[-1] == '1':  # Checks if the first or last digit is a 1
            count += 1  
    return count