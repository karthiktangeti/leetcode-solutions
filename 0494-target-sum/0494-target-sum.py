class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        def dfs(index,sum1):
            if index == len(nums):
                return 1 if sum1 == target else 0
            if (index,sum1) in memo:
                return memo[(index,sum1)]
            memo[(index,sum1)] = (
                dfs(index + 1,sum1 + nums[index]) + 
                dfs(index + 1,sum1 - nums[index]))
            return memo[(index,sum1)]
        return dfs(0,0)
        
        