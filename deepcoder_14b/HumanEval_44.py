def int_to_str(n, base):
    if n == 0:
        return '0'
    
    digits = []
    is_negative = False
    
    # Handle negative numbers
    if n < 0:
        is_negative = True
        n = abs(n)
    
    while n > 0:
        rem = n % base
        if rem < 10:
            rem_char = str(rem)
        else:
            rem_char = chr(ord('A') + rem - 10)  # For bases up to 36
        digits.append(rem_char)
        n = n // base
    
    # If the number was negative, prepend the minus sign
    if is_negative:
        digits.append('-')
    
    # Reverse the digits to get the correct order and join them
    return ''.join(reversed(digits))