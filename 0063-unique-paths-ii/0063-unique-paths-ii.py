class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])
        memo = {}
        def dfs(i,j):
            if i < 0 or i >= row or j < 0 or j >= col:
                return 0
            if obstacleGrid[i][j] == 1:
                return 0
            if i == row - 1 and j == col - 1:
                return 1
            if (i,j) in memo:
                return memo[(i,j)]
            memo[(i,j)] =  dfs(i + 1,j) + dfs(i,j + 1)
            return memo[(i,j)]
        return dfs(0,0)
         