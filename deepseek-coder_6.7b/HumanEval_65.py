def circular_shift(x, shift):
    digits = list(str(x))
    if shift >= len(digits):
        return ''.join(reversed(digits))
    
    rotated_digits = digits[shift:] + digits[:shift]
    return ''.join(rotated_digits)