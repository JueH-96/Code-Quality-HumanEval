def get_row(lst, x):
    """
    You are given a 2 dimensional data, as a nested lists,
    which is similar to matrix, however, unlike matrices,
    each row may contain a different number of columns.
    Given lst, and integer x, find integers x in the list,
    and return list of tuples, [(x1, y1), (x2, y2) ...] such that
    each tuple is a coordinate - (row, columns), starting with 0.
    Sort coordinates initially by rows in ascending order.
    Also, sort coordinates of the row by columns in descending order.
    
    Examples:
    get_row([
      [1,2,3,4,5,6],
      [1,2,3,4,1,6],
      [1,2,3,4,5,1]
    ], 1) == [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]
    get_row([], 1) == []
    get_row([[], [1], [1, 2, 3]], 3) == [(2, 2)]
    """
    # list to store the coordinates grouped by row index
    row_coords = {}
    
    # iterate each row and its index
    for i, row in enumerate(lst):
        # iterate each column index and value
        for j, val in enumerate(row):
            if val == x:
                if i not in row_coords:
                    row_coords[i] = []
                row_coords[i].append((i, j))
                
    result = []
    # sort the rows ascending by row index
    for row_index in sorted(row_coords.keys()):
        # sort this row's coordinates by column descending
        coords = sorted(row_coords[row_index], key=lambda t: t[1], reverse=True)
        result.extend(coords)
    
    return result