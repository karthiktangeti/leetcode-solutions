class Solution(object):
    def subsetXORSum(self, nums):
        total = 0
        def dfs(i,xor_t):
            nonlocal total
            if i == len(nums):
                total += xor_t
                return 
            dfs(i + 1,xor_t ^ nums[i])
            dfs(i + 1,xor_t)
        dfs(0,0)
        return total