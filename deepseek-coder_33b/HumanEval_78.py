def hex_key(num):
    def is_prime(n):
        if n < 2: return False
        if n == 2 or n == 3 or n == 5 or n == 7 or n == 11 or n == 13: return True
        if n % 2 == 0 or n % 3 == 0 or n % 5 == 0 or n % 7 == 0 or n % 11 == 0 or n % 13 == 0: return False
        i, w = 5, 2
        while i * i <= n:
            if n % i == 0: return False
            i += w
            w = 6 - w
        return True
        
    count = 0
    for c in num.upper():
        d = int(c, 16)
        if is_prime(d):
            count += 1
    return count