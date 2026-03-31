def get_row(lst, x):
    coordinates = []
    for i in range(len(lst)):
        row = lst[i]
        for j in range(len(row)):
            if row[j] == x:
                coordinates.append((i, j))
    # Sort by row ascending, then by column descending
    coordinates.sort(key=lambda coord: (coord[0], -coord[1]))
    return coordinates