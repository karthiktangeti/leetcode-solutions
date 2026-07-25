from collections import deque
class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        if grid[0][0] == 1:
            return -1
        cols = len(grid[0])
        rows = len(grid)
        dis = [[float("inf")] * cols for i in range(rows)]
        queue = deque()
        queue.append([1,0,0])
        dis[0][0] = 1
        while queue:
            d,i,j = queue.popleft()
            for r,c in [[1,0],[0,1],[-1,1],[1,-1],[1,1],[-1,-1],[0,-1],[-1,0]]:
                n_r,n_c = i + r,c + j
                if n_r < 0 or n_r >= rows or n_c < 0 or n_c >= cols:
                    continue
                if grid[n_r][n_c] == 1:
                    continue
                dist_trev = d + 1
                if dist_trev < dis[n_r][n_c]:
                    dis[n_r][n_c] = dist_trev
                    queue.append((dist_trev,n_r,n_c))
        if dis[rows -1][cols - 1] == float("inf"):
            return -1
        return dis[rows - 1][cols - 1]
        