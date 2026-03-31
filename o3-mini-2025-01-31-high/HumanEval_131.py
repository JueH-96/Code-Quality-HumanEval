def digits(n):
    product = 1
    found = False
    while n:
        digit = n % 10
        if digit % 2 == 1:
            product *= digit
            found = True
        n //= 10
    return product if found else 0