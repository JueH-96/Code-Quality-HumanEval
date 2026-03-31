from collections import deque
def minPath(grid, k):
    N = len(grid)
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)] # up, down, left, right
    
    def bfs(start):
        queue = deque([(start, [])])
        visited = {start}
        
        while queue:
            cell, path = queue.popleft()
            
            if len(path) == k: # we have a path of length 'k'
                return path
                
            for dr, dc in dirs:
                nr, nc = cell[0] + dr, cell[1] + dc 
                if 0 <= nr < N and 0 <= nc < N: # check if we can go off the grid
                    new_cell = (nr, nc)
                    if new_cell not in visited:
                        queue.append((new_cell, path + [grid[nr][nc]]))
                        visited.add(new_cell)
    # get minpath for each cell as starting point
    minPath = None
    for r in range(N):
        for c in range(N):
            currPath = bfs((r,c))
            if not minPath or currPath < minPath: 
                minPath = currPath
                
    return minPath