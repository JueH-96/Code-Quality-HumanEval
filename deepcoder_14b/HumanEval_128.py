def prod_signs(arr):
    if not arr:
        return None
    sum_abs = sum(abs(x) for x in arr)
    product_signs = 1
    for num in arr:
        if num == 0:
            product_signs = 0
            break
        else:
            sign = 1 if num > 0 else -1
            product_signs *= sign
    return sum_abs * product_signs