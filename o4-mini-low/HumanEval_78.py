def hex_key(num):
    """You have been tasked to write a function that receives 
    a hexadecimal number as a string and counts the number of hexadecimal 
    digits that are primes."""
    prime_digits = {'2', '3', '5', '7', 'B', 'D'}
    return sum(1 for c in num if c in prime_digits)