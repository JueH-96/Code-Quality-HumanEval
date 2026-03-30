def skjkasdkd(lst):
    """You are given a list of integers.
    You need to find the largest prime value and return the sum of its digits.
    """
    def is_prime(n):
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

    largest_prime = None
    for num in lst:
        if is_prime(num):
            if largest_prime is None or num > largest_prime:
                largest_prime = num

    if largest_prime is None:
        return 0

    return sum(int(digit) for digit in str(largest_prime))