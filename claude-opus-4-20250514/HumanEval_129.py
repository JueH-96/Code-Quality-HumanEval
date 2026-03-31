def minPath(grid, k):
    """
    Given a grid with N rows and N columns (N >= 2) and a positive integer k, 
    each cell of the grid contains a value. Every integer in the range [1, N * N]
    inclusive appears exactly once on the cells of the grid.

    You have to find the minimum path of length k in the grid. You can start
    from any cell, and in each step you can move to any of the neighbor cells,
    in other words, you can go to cells which share an edge with you current
    cell.
    Please note that a path of length k means visiting exactly k cells (not
    necessarily distinct).
    You CANNOT go off the grid.
    A path A (of length k) is considered less than a path B (of length k) if
    after making the ordered lists of the values on the cells that A and B go
    through (let's call them lst_A and lst_B), lst_A is lexicographically less
    than lst_B, in other words, there exist an integer index i (1 <= i <= k)
    such that lst_A[i] < lst_B[i] and for any j (1 <= j < i) we have
    lst_A[j] = lst_B[j].
    It is guaranteed that the answer is unique.
    Return an ordered list of the values on the cells that the minimum path go through.

    Examples:

        Input: grid = [ [1,2,3], [4,5,6], [7,8,9]], k = 3
        Output: [1, 2, 1]

        Input: grid = [ [5,9,3], [4,1,6], [7,8,2]], k = 1
        Output: [1]
    """
    n = len(grid)
    
    # Find all possible starting positions and their values
    positions = []
    for i in range(n):
        for j in range(n):
            positions.append((grid[i][j], i, j))
    
    # Sort positions by value to start from smallest values
    positions.sort()
    
    # Direction vectors for moving to adjacent cells
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    # Try starting from each position
    min_path = None
    
    for start_val, start_i, start_j in positions:
        # Use BFS/DFS to find all paths of length k from this starting position
        def find_paths(i, j, path, remaining):
            if remaining == 0:
                return [path[:]]
            
            paths = []
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < n and 0 <= nj < n:
                    path.append(grid[ni][nj])
                    paths.extend(find_paths(ni, nj, path, remaining - 1))
                    path.pop()
            
            return paths
        
        # Find all paths of length k starting from (start_i, start_j)
        all_paths = find_paths(start_i, start_j, [start_val], k - 1)
        
        # Find the lexicographically smallest path from this starting position
        if all_paths:
            local_min = min(all_paths)
            if min_path is None or local_min < min_path:
                min_path = local_min
    
    return min_path