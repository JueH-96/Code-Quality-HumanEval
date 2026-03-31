def find_coordinates(lst, x):
    # Collect all coordinates where lst[i][j] == x
    coords = [(i, j) for i in range(len(lst)) for j in range(len(lst[i])) if lst[i][j] == x]
    
    # Sort by row ascending, then column descending within the same row
    sorted_coords = sorted(coords, key=lambda t: (t[0], -t[1]))
    
    return sorted_coords