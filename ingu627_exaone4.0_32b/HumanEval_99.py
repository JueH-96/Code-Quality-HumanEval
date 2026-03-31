def closest_integer(value):
    num = float(value)
    integer_part = int(num)
    fractional_part = num - integer_part
    
    if num >= 0:
        if fractional_part > 0.5:
            return integer_part + 1
        elif fractional_part < 0.5:
            return integer_part
        else:
            return integer_part + 1
    else:
        if fractional_part < -0.5:
            return integer_part - 1
        elif fractional_part > -0.5:
            return integer_part
        else:
            return integer_part - 1