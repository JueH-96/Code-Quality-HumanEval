def make_a_pile(n):
    result = []
    current = n
    for _ in range(n):
        result.append(current)
        if n % 2 == 0:
            current += 2
        else:
            current += 1
    return result