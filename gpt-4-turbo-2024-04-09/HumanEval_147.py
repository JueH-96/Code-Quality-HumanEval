def get_max_triples(n):
    # Create the array a based on the given formula
    a = [i * i - i + 1 for i in range(1, n + 1)]
    
    # Count the remainders when divided by 3
    remainder_count = [0, 0, 0]
    for value in a:
        remainder_count[value % 3] += 1
    
    # Calculate the number of valid triples
    # We need the sum of three numbers to be a multiple of 3
    # This can happen in the following scenarios:
    # 1. All three numbers have the remainder 0 when divided by 3
    # 2. One number has remainder 0, one has remainder 1, and one has remainder 2
    count = 0
    # Case 1: All three numbers are 0 mod 3
    if remainder_count[0] >= 3:
        count += remainder_count[0] * (remainder_count[0] - 1) * (remainder_count[0] - 2) // 6
    # Case 2: One number is 0 mod 3, one is 1 mod 3, one is 2 mod 3
    if remainder_count[0] >= 1 and remainder_count[1] >= 1 and remainder_count[2] >= 1:
        count += remainder_count[0] * remainder_count[1] * remainder_count[2]
    
    return count