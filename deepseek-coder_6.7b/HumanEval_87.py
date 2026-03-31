def get_row(lst, x):
    if not lst or all(not row for row in lst): return []
    coords = [(i, j) for i, row in enumerate(lst) for j, val in enumerate(row) if val == x]
    return sorted(coords, key=lambda coord: (coord[0], -coord[1]))