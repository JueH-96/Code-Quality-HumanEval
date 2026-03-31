def hex_key(num):
    """Returns the count of hexadecimal digits in `num` that correspond to
    prime decimal values (2, 3, 5, 7, 11, 13 -> '2','3','5','7','B','D')."""
    primes_hex = {'2', '3', '5', '7', 'B', 'D'}
    return sum(1 for ch in num.upper() if ch in primes_hex)