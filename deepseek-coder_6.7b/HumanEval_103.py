def rounded_avg(n, m):
    if n > m:
        return -1
    avg = round((m + n) / 2)
    return bin(avg).replace("0b", "")