def solve(N):
    """Given a positive integer N, return the total sum of its digits in binary."""
    # Convert the number to binary and remove the '0b' prefix
    binary_representation = bin(N)[2:]
    # Calculate the sum of the digits in the binary representation
    digit_sum = sum(int(digit) for digit in binary_representation)
    # Convert the sum to a binary string
    return bin(digit_sum)[2:]