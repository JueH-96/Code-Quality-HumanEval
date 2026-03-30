def skjkasdkd(lst):
    def is_prime(n):
        if n <= 1:
            return False
        if n == 2 or n == 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while (i * i) <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    max_prime = -1
    for num in lst:
        if is_prime(num):
            max_prime = max(max_prime, num)

    if max_prime == -1:
        return 0

    return sum(int(digit) for digit in str(max_prime))