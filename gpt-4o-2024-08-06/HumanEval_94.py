def skjkasdkd(lst):
    """You are given a list of integers.
    You need to find the largest prime value and return the sum of its digits.
    """
    def is_prime(n):
        """Check if a number is prime."""
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def sum_of_digits(n):
        """Return the sum of the digits of a number."""
        return sum(int(digit) for digit in str(n))

    # Find the largest prime in the list
    largest_prime = None
    for num in lst:
        if is_prime(num):
            if largest_prime is None or num > largest_prime:
                largest_prime = num

    # If no prime number is found, return 0
    if largest_prime is None:
        return 0

    # Return the sum of the digits of the largest prime
    return sum_of_digits(largest_prime)