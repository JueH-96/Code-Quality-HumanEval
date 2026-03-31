def digits(n):
    product = 1
    any_odd = False
    for c in str(n):
        digit = int(c)
        if digit % 2 != 0:
            product *= digit
            any_odd = True
    return product if any_odd else 0