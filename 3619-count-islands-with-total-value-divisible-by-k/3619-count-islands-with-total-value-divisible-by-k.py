class Solution(object):
    def countIslands(self, grid, k):
        if not grid:
            return 0
        def dfs(r,c):
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
                return 0
            if grid[r][c] == 0:
                return 0
            sum1 = grid[r][c]
            grid[r][c] = 0
            return (
                sum1
                + dfs(r-1,c)
                + dfs(r+1,c)
                + dfs(r,c-1)
                + dfs(r,c+1)
            ) 
        count = 0    
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 0:
                    if dfs(i,j) % k == 0:
                        count += 1
        return count
        