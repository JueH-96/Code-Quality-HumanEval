def minPath(grid, k):
    """
    Given a grid with N rows and N columns (N >= 2) and a positive integer k,
    each cell of the grid contains a value. Every integer in the range [1, N * N]
    inclusive appears exactly once on the cells of the grid.

    You have to find the minimum path of length k in the grid. You can start
    from any cell, and in each step you can move to any of the neighbor cells,
    in other words, you can go to cells which share an edge with your current
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
    # dp[i][r][c] will store the lexicographically smallest tuple of length i starting at (r, c)
    dp = [[[None] * n for _ in range(n)] for _ in range(k + 1)]

    # Base case: paths of length 1
    for r in range(n):
        for c in range(n):
            dp[1][r][c] = (grid[r][c],)

    # Helper for valid neighbors
    def neighbors(r, c):
        for rr, cc in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
            if 0 <= rr < n and 0 <= cc < n:
                yield rr, cc

    # Fill dp for path lengths from 2 to k
    for length in range(2, k + 1):
        for r in range(n):
            for c in range(n):
                best = None
                for nr, nc in neighbors(r, c):
                    if best is None or dp[length - 1][nr][nc] < best:
                        best = dp[length - 1][nr][nc]
                dp[length][r][c] = (grid[r][c],) + best

    # Find the lexicographically smallest among all dp[k][r][c]
    ans = None
    for r in range(n):
        for c in range(n):
            if ans is None or dp[k][r][c] < ans:
                ans = dp[k][r][c]

    return list(ans)