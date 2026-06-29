class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        ans = 0
        def dfs(i,j,sum1):
            nonlocal ans
            ans = max(ans,sum1)
            gold = grid[i][j]
            grid[i][j] = 0
            for x, y in [(0,-1),(0,1),(-1,0),(1,0)]:
                nx,ny = i + x,j + y
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] != 0:
                    dfs(nx,ny,sum1 + grid[nx][ny])
            grid[i][j] = gold
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 0:
                    dfs(i,j,grid[i][j])
        return ans
        