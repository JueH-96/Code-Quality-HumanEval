def count_set_bits(n):
    # Convert the integer to its binary string representation without '0b' prefix
    binary_str = bin(n)[2:]
    # Count the number of '1's in the binary string
    ones_count = binary_str.count('1')
    # Return the count as a string
    return str(ones_count)