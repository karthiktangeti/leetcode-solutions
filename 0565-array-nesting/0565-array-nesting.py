class Solution(object):
    def arrayNesting(self, nums):
        visited = set()
        ans = 0
        def dfs(node):
            if node in visited:
                return 0
            visited.add(node)
            return 1 + dfs(nums[node])
        for i in range(len(nums)):
            if i not in visited:
                ans = max(ans,dfs(i))
        return ans
        