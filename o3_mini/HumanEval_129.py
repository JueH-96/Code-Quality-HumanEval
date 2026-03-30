import heapq

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
    n = len(grid)
    # Directions: down, up, right, left.
    moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    # Priority queue: each element is (path_sequence, row, col, steps)
    heap = []
    # Visited dictionary to record the best lexicographical sequence for a given state (r, c, steps)
    visited = {}
    
    # Initialize with every cell as a starting position.
    for i in range(n):
        for j in range(n):
            seq = (grid[i][j],)
            state = (i, j, 1)
            visited[state] = seq
            heapq.heappush(heap, (seq, i, j, 1))
    
    # Use a lexicographical Dijkstra-like approach.
    while heap:
        seq, i, j, steps = heapq.heappop(heap)
        if steps == k:
            return list(seq)
        for di, dj in moves:
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < n:
                new_seq = seq + (grid[ni][nj],)
                new_state = (ni, nj, steps + 1)
                if new_state not in visited or new_seq < visited[new_state]:
                    visited[new_state] = new_seq
                    heapq.heappush(heap, (new_seq, ni, nj, steps + 1))
    
    # Should never reach here as answer is guaranteed to exist.
    return []