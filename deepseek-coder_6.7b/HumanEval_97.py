def multiply(a, b):
    # get last digit of each number by modulus 10
    unit_digit_a = abs(a) % 10
    unit_digit_b = abs(b) % 10
    
    return unit_digit_a * unit_digit_b