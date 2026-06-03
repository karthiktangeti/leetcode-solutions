class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        max_row = []
        max_col = []
        for i in range(len(grid)):
            max_row.append(max(grid[i]))
        for i in range(len(grid[0])):
            max_el = float("-inf")
            for j in range(len(grid)):
                max_el = max(max_el,grid[j][i])
            max_col.append(max_el)
        sum1 = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                el = min(max_row[i],max_col[j])
                sum1 += el - grid[i][j]
        return sum1
        