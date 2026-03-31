def get_row(lst, x):
    coordinates = []
    for row_index, row in enumerate(lst):
        # Find all column indices in the current row where the element is x
        col_indices = [col_index for col_index, value in enumerate(row) if value == x]
        # Sort column indices in descending order
        col_indices.sort(reverse=True)
        # Add coordinates to the list
        for col_index in col_indices:
            coordinates.append((row_index, col_index))
    return coordinates