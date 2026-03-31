def is_bored(S):
    count = 0   # Initialize counter for boredoms to zero.
    S = S.split('. ')  # Split the string into sentences by '. '
    
    for sentence in S:
        if sentence[0] == "I":  # Check if first word is "I"
            count += 1   # If it is, increment counter
            
    return count   # Return final count of boredoms