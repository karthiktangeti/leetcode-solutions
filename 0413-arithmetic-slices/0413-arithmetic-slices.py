class Solution(object):
    def numberOfArithmeticSlices(self, nums):
        ans = 0
        curr = 0
        for i in range(2,len(nums)):
            if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
                curr += 1
                ans += curr
            else:
                curr = 0
        return ans
        