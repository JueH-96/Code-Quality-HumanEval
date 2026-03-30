def get_odd_collatz(n):
    """
    Given a positive integer n, return a sorted list that has the odd numbers in collatz sequence.
    """
    odd_numbers = set()
    while n != 1:
        if n % 2 != 0:
            odd_numbers.add(n)
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
    odd_numbers.add(1)  # Add 1 as it is always part of the sequence
    return sorted(odd_numbers)