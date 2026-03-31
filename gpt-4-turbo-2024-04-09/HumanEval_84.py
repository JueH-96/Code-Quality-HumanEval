def solve(N):
    """Given a positive integer N, return the total sum of its digits in binary."""
    sum_of_digits = sum(int(digit) for digit in str(N))
    return bin(sum_of_digits)[2:]