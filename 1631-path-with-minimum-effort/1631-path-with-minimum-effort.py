import heapq
class Solution(object):
    def minimumEffortPath(self, heights):
        rows = len(heights)
        cols = len(heights[0])
        path = [[float("inf")] * cols for i in range(rows)]
        pq = [(0,0,0)]
        path[0][0] = 0
        while pq:
            eff,i,j = heapq.heappop(pq)
            if i == rows -1 and j == cols -1:
                return eff
            for x,y in [[-1,0],[0,-1],[1,0],[0,1]]:
                n_r,n_c = i + x,j + y
                if n_r < 0 or n_r >= rows or n_c < 0 or n_c >= cols:
                    continue
                new_eff = max(eff,abs(heights[i][j] - heights[n_r][n_c]))
                if new_eff < path[n_r][n_c]:
                    path[n_r][n_c] = new_eff
                    heapq.heappush(pq,(new_eff,n_r,n_c))
        return 0
        