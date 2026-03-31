def tribonacci(n):
    t = [0, 1, 1] + [0]* (n-2) # Initialize Tribonacci sequence with first three numbers and fill remaining places with zeroes.
    
    for i in range(3, n+1): # Compute Tribonacci values up to the given number 'n'.
        t[i] = t[i-1] + t[i-2] + t[i-3] 
        
    return t[:n+1] # Return list of first n + 1 numbers.