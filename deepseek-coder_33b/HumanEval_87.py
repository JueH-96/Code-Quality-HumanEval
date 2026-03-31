def get_row(lst, x):
    result = []
    for i in range(len(lst)):
        for j in reversed(range(len(lst[i]))):
            if lst[i][j] == x:
                result.append((i, j))
    return sorted(result)