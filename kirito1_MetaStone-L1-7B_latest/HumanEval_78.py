def hex_key(num):
    allowed = {'2', '3', '5', '7', 'B', 'D'}
    count = 0
    for c in num:
        if c in allowed:
            count += 1
    return count