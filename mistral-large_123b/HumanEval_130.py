def tri(n):
    if n == 0:
        return [1]
    elif n == 1:
        return [1, 3]

    trib = [1, 3]
    for i in range(2, n + 1):
        if i % 2 == 0:
            trib.append(1 + i / 2)
        else:
            next_val = trib[i - 1] + trib[i - 2] + (trib[i] if i < len(trib) else 1 + (i + 1) / 2)
            trib.append(next_val)
    return trib