import math

def is_power(n, x):
    if n == 0:
        return False if x != 0 else True
    elif x == 0:
        return True
    
    abs_n = abs(n)
    abs_x = abs(x)
    
    # Special case where |n| is 1: any power would be ±1
    if (abs_n == 1) and ((x == 1) or (x == -1)):
        return True
    
    max_k = int(math.log(2 * abs_x, abs_n)) + 2
    for k in range(-max_k, max_k + 1):
        try:
            product = pow(n, k)
        except OverflowError:
            continue
        
        if (abs(product) == abs_x) and ((product * x >= 0) or x == 0):
            return True
    
    return False