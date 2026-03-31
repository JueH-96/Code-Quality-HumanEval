def median(l):
    sorted_l = sorted(l)
    n = len(sorted_l)
    if n % 2 == 1:
        return sorted_l[n // 2]
    else:
        mid_left = sorted_l[(n // 2) - 1]
        mid_right = sorted_l[n // 2]
        return (mid_left + mid_right) / 2