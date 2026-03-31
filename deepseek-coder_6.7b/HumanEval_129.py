import heapq

def minPath(grid, k):
    pq = [] # Priority Queue
    N = len(grid) 
    
    for i in range(N):
        for j in range(N):
            if len(pq) < k: 
                heapq.heappush(pq, (grid[i][j], i, j)) # Pushing the grid value and its coordinates into priority queue
            else:  
                if pq[0][0] < grid[i][j]:  # Comparing top of the priority queue with current cell's value
                    heapq.heappop(pq)    # If it is smaller, then pop it from priority queue
                    heapq.heappush(pq, (grid[i][j], i, j))   # Push current grid value and its coordinates into priority queue
    
    res = [] 
    while pq:   # Getting the values from priority queue in lexicographical order
        val, i, j = heapq.heappop(pq)
        res.append(val)
        
    return res[::-1]  # Returning reversed result as we are inserting smallest value at front of pq and required sequence is reverse of this