def digits(n):
    product = 1
    has_odd_digit = False
    for digit in str(n):
        int_digit = int(digit)
        if int_digit % 2 != 0:
            product *= int_digit
            has_odd_digit = True
    return product if has_odd_digit else 0