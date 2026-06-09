class Solution(object):
    def matrixBlockSum(self, mat, k):
        n = len(mat)
        m = len(mat[0])
        prefix = [[0] * (m + 1) for i in range(n + 1)]
        for i in range(1,n + 1):
            for j in range(1,m + 1):
                prefix[i][j] = (mat[i- 1][j - 1] + prefix[i - 1][j] + prefix[i][j - 1] - prefix[i - 1][j - 1])
        ans = [[0] * m for i in range(n)]
        for i in range(n):
            for j in range(m):
                r1 = max(0,i -k)
                c1 = max(0,j - k)
                r2 = min(n - 1,i + k)
                c2 = min(m - 1,j + k)
                ans[i][j] = (prefix[r2 + 1][c2 + 1] + prefix[r1][c1] - prefix[r1][c2 + 1] - prefix[r2 +1][c1])
        return ans
        