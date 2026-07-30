class Solution(object):
    def uniquePaths(self, m, n):
        row = m
        col = n
        memo = {}
        def dfs(i,j):
            if i < 0 or i >= row or j < 0 or j >= col:
                return 0
            if i == row - 1 or j == col - 1:
                return 1
            if (i,j) in memo:
                return memo[(i,j)]
            memo[(i,j)] = dfs(i + 1,j) + dfs(i,j + 1)
            return memo[(i,j)]
        return dfs(0,0)        