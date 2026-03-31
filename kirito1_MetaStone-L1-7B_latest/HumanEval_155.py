def even_odd_count(num):
    num = abs(num)
    s = str(num)
    even = 0
    odd = 0
    for c in s:
        digit = int(c)
        if digit % 2 == 0:
            even += 1
        else:
            odd += 1
    return (even, odd)