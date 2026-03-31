def is_power_of(x, n):
    # Handle special cases where n is 0
    if n == 0:
        return x == 0
    
    # Check for trivial cases and handle n = 1 or -1
    if x == 1:
        # Any number to the power of 0 is 1, but since we're checking exponents >=1,
        # only possible if n itself is 1 (since 1^k=1) or (-1)^even =1
        return n in {1, -1}
    elif x == -1:
        # Only possible if n is -1 and exponent is odd
        return n == -1
    
    current = n
    exponent = 1
    while True:
        if current == x:
            return True
        # Check if the next step would exceed, to prevent infinite loops
        next_current = current * n
        if abs(next_current) > abs(x):
            break
        current = next_current
        exponent += 1
    
    return False

# Example usage:
# print(is_power_of(8, 2))  # Output: True (since 2^3=8)
# print(is_power_of(-8, -2))  # Output: True (since (-2)^3=-8)