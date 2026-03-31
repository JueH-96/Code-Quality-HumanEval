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
    # Initialize an empty list to store the coordinates
    coordinates = []

    # Iterate over each row in the list
    for i, row in enumerate(lst):
        # Iterate over each element in the row
        for j, num in enumerate(row):
            # Check if the current number matches the target number
            if num == x:
                # If it does, add its coordinates to the list
                coordinates.append((i, j))

    # Sort the coordinates first by rows in ascending order, then by columns in descending order
    sorted_coordinates = sorted(coordinates, key=lambda coord: (coord[0], -coord[1]))

    return sorted_coordinates