def digits(n):
    product = 1
    has_odd = False
    
    for digit in str(n):
        d = int(digit)
        if d % 2 != 0:
            product *= d
            has_odd = True
            
    return product if has_odd else 0