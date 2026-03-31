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
    """
    N = len(grid)
    # Find the minimum value in the grid and its positions
    min_val = float('inf')
    positions = set()
    for i in range(N):
        for j in range(N):
            v = grid[i][j]
            if v < min_val:
                min_val = v
                positions = {(i, j)}
            elif v == min_val:
                positions.add((i, j))
    # Build the lexicographically minimum path
    path = [min_val]
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for _ in range(k - 1):
        next_val = float('inf')
        next_positions = set()
        for (i, j) in positions:
            for di, dj in dirs:
                ni, nj = i + di, j + dj
                if 0 <= ni < N and 0 <= nj < N:
                    v = grid[ni][nj]
                    if v < next_val:
                        next_val = v
                        next_positions = {(ni, nj)}
                    elif v == next_val:
                        next_positions.add((ni, nj))
        path.append(next_val)
        positions = next_positions
    return path