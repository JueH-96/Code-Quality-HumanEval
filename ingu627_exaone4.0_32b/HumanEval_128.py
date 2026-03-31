def prod_signs(arr):
    if not arr:
        return None
    sign_product = 1
    sum_abs = 0
    for num in arr:
        if num > 0:
            sign_product *= 1
        elif num < 0:
            sign_product *= -1
        else:
            sign_product *= 0
        sum_abs += abs(num)
    return sign_product * sum_abs