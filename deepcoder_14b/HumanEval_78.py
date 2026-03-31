def hex_key(num):
    primes = {2, 3, 5, 7, 11, 13}
    count = 0
    for c in num:
        dec = int(c, 16)
        if dec in primes:
            count += 1
    return count