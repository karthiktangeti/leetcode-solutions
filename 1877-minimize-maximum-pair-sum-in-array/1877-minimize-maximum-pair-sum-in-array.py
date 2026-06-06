class Solution(object):
    def minPairSum(self, nums):
        nums.sort()
        l = 0
        r = len(nums) - 1
        sum1 = 0
        max_sum = float("-inf")
        while l < r:
            sum1 = nums[l] + nums[r]
            max_sum = max(max_sum,sum1)
            sum1 = 0
            l += 1
            r -= 1
        return max_sum
            
        