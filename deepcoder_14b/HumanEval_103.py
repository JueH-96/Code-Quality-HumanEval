def rounded_binary(n, m):
    lower = min(n, m)
    higher = max(n, m)
    k = higher - lower + 1
    total = (lower + higher) * k // 2
    average = total / k
    rounded_val = round(average)
    binary_str = format(rounded_val, 'b')
    return binary_str