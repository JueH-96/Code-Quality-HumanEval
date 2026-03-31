def rounded_avg(n, m):
    if n > m:
        return -1
    average = (n + m) / 2
    rounded = round(average)
    binary_str = bin(rounded)[2:]
    return f'0b{binary_str}'