class Solution(object):
    def pathExistenceQueries(self, n, nums, maxDiff, queries):
        components = [0] * n
        comp = 0
        for i in range(1,n):
            if abs(nums[i] - nums[i - 1]) > maxDiff:
                comp += 1
            components[i] = comp
        res = []
        for u,v in queries:
            if components[u] == components[v]:
                res.append(True)
            else:
                res.append(False)
        return res
        