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
    N = len(grid)
    # find the minimum value cell to start
    min_val = grid[0][0]
    si = sj = 0
    for i in range(N):
        for j in range(N):
            if grid[i][j] < min_val:
                min_val = grid[i][j]
                si, sj = i, j
    path = [min_val]
    ci, cj = si, sj
    moves = [(1,0),(-1,0),(0,1),(0,-1)]
    # build the path greedily
    for _ in range(1, k):
        best_val = float('inf')
        ni_best = nj_best = None
        for di, dj in moves:
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < N:
                v = grid[ni][nj]
                if v < best_val:
                    best_val = v
                    ni_best, nj_best = ni, nj
        path.append(best_val)
        ci, cj = ni_best, nj_best
    return path