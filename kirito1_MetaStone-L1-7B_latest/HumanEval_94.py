def skjkasdkd(lst):
    def is_prime(n):
        if n <= 1:
            return False
        elif n <= 3:
            return True
        elif n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        w = 2
        while i * i <= n:
            if n % i == 0:
                return False
            i += w
            w = 6 - w
        return True

    current_largest = None
    for num in lst:
        if is_prime(num):
            if current_largest is None or num > current_largest:
                current_largest = num
    if current_largest is None:
        return 0
    return sum(int(d) for d in str(current_largest))