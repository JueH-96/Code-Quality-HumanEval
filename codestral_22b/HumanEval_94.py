def skjkasdkd(lst):
    def is_prime(n):
        if n <= 1:
            return False
        elif n == 2:
            return True
        else:
            for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                    return False
            return True

    primes = [x for x in lst if is_prime(x)]
    if not primes:
        return None
    largest_prime = max(primes)
    sum_of_digits = sum(int(digit) for digit in str(largest_prime))
    return sum_of_digits