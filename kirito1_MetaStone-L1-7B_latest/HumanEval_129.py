import heapq

def find_smallest_path(grid, K):
    if not grid:
        return []
    
    rows = len(grid)
    cols = len(grid[0])
    
    # Directions: right, left, down, up (to manage all four moves)
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    heap = []
    best = dict()  # Maps (i,j,m) to the lex smallest sequence
    
    # Initialize with all single-step paths
    for i in range(rows):
        for j in range(cols):
            seq = [grid[i][j]]
            state = (i, j, len(seq))
            if state not in best or best[state] > seq:
                heapq.heappush(heap, (seq.copy(), i, j))
                best[state] = seq.copy()
    
    while heap:
        current_seq, i, j = heapq.heappop(heap)
        m = len(current_seq)
        
        # Check if we have found the path of length K
        if m == K:
            return current_seq
        
        # If remaining steps can't form a longer path than needed, skip
        if (K - m) < 0:
            continue
        
        for di, dj in directions:
            ni = i + di
            nj = j + dj
            
            if 0 <= ni < rows and 0 <= nj < cols:
                new_val = grid[ni][nj]
                new_seq = current_seq.copy()
                new_seq.append(new_val)
                new_m = m + 1
                
                state = (ni, nj, new_m)
                
                # Check if this new state is better than any existing
                existing = best.get(state, None)
                if existing is not None:
                    if new_seq <= existing:
                        continue
                else:
                    pass  # No existing seq, no need to compare
                
                # Add the new sequence only if it's lex smaller than all others at this state and step
                heapq.heappush(heap, (new_seq.copy(), ni, nj))
                best[state] = new_seq.copy()
    
    # If we exhausted heap without returning, K is not reachable
    return []