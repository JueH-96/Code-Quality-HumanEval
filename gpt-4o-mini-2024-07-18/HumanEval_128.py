def prod_signs(arr):
    if not arr:
        return None
    
    product_sign = 1
    magnitude_sum = 0
    
    for num in arr:
        if num > 0:
            magnitude_sum += num
        elif num < 0:
            magnitude_sum += -num
            product_sign *= -1
        else:
            return 0
    
    return product_sign * magnitude_sum