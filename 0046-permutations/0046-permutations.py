class Solution(object):
    def permute(self, nums):
        result = []
        def dfs(path):
            if len(path) == len(nums):
                result.append(path[:])
                return 
            for i in nums:
                if i not in path:
                    path.append(i)
                    dfs(path)
                    path.pop()
        dfs([])
        return result
        