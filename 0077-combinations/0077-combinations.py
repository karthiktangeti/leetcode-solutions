class Solution(object):
    def combine(self, n, k):
        res = []
        def dfs(path,c):
            if len(path) == k:
                res.append(path[:])
                return 
            for j in range(c,n + 1):
                path.append(j)
                dfs(path,j + 1)
                path.pop()


        dfs([],1)
        return res
        