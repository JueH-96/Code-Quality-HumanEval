from heapq import heappush, heappop

def minPath(grid, k):
    N = len(grid)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def in_bounds(x, y):
        return 0 <= x < N and 0 <= y < N

    min_heap = []
    for i in range(N):
        for j in range(N):
            heappush(min_heap, (grid[i][j], [(i, j)], grid[i][j]))

    while min_heap:
        _, path, path_sum = heappop(min_heap)

        if len(path) == k:
            return [grid[x][y] for x, y in path]

        last_x, last_y = path[-1]

        for dx, dy in directions:
            new_x, new_y = last_x + dx, last_y + dy
            if in_bounds(new_x, new_y):
                new_path = path + [(new_x, new_y)]
                heappush(min_heap, (tuple(new_path), new_path, path_sum * 100 + grid[new_x][new_y]))