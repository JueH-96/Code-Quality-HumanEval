def tri(n):
    if n == 0: return [3]
    elif n == 1: return [3, 2]
    else:
        trib = [3, 2, 8] + [0] * (n-2)
        for i in range(3, n+1):
            if i % 2 == 0:
                trib[i] = 1 +  i // 2
            else:
                trib[i] = trib[i - 1] + trib[i - 2] + trib[i - 3]
        return trib[:n+1]