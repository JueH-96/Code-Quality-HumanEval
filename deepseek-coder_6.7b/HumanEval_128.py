def prod_signs(arr):
    if not arr: return None     # If array is empty, return None
    
    sign = 1                     # Initialize sign to positive
    sumMag = 0                   # Initialize sum of magnitudes to zero
        
    for num in arr:              
        sign *= -1 if num < 0 else 1   # Multiply current sign by -1 or keep it as 1, depending on the number's sign
        sumMag += abs(num)              # Add magnitude of number to sum
        
    return sign*sumMag                # Return calculated result