def prod_signs(arr):
    if not arr:
        return None
    sign = 1
    mag = []
    for i in arr:
        if i < 0:
            sign *= -1
        elif i == 0:
            return 0
        else:
            mag.append(i)
    sum_mag = sum(mag)
    return sign * sum_mag