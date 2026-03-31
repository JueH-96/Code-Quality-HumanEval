def make_a_pile(n):
    result = []
    current_stones = n
    for i in range(n):
        result.append(current_stones)
        if current_stones % 2 == 0:
            current_stones += 2
        else:
            current_stones += 2
    return result