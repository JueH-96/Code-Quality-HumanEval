def max_fill(grid, capacity):  
    import sys  # Python in-built module for system related operations    
        
    directions = [[-1,-1], [-1,0], [-1,1],[0,-1], [0,0] ,[0,1], [1,-1], [1,0], [1,1]]  # possible moves in a grid for water bucket.    
        
    def dfs(i, j):   # Depth First Search function to find all connected components of 'O's into which an empty space can be filled by waters with given capacity using DFS traversal method over the provided Grid/Matrix 1) If a component has been visited (visited[x][y]), then return.
        if i < 0 or j <  0 or i >= len(grid )or j>=len(grid[i]) or grid[i][j]=='X':    # Checking for out of boundary conditions 2) If the cell is already visited (visited[]), then return.
            return False      
        if grid[i][j]:     # For cells which are 'O', set them to unreachable state and continue exploration in all available directions by recursively calling dfs().  3 &4). Continue until you find either a "0" or no reach of outbound water, then return.
            if i == 0  :    sys.exit(1)       # If we are at the source cell (i=='O'), exit from function as there is only one valid path possible to fill all cells with given capacity and hence it will be already filled by waters in next dfs() call or else infinite loops may occur due to recursion depth limit exceeded. 
            grid[i][j] = 0   # Mark this cell visited so that we do not visit same node again while calling function on current cells connected components, which might lead into a wrong answer if it's already marked as 'X'.   5) If all water can be filled (current i or j is last row/column), return true.
        for dir in directions:   # Go to each direction 6 and then recursive call dfs() with the next cell after moving into that particular position, if current move leads us inside a new connected component of 'O's'.   7) If it reaches at last row/column without any water source (i==last), return true.
            dfsf( i + dir[0], j+dir[1])  # Call DFS on next cell in this direction, if current move leads us inside a new connected component of 'O's'.   8) Otherwise continue recursion until we find all water sources and empty cells can be filled with given capacity by using bucket.