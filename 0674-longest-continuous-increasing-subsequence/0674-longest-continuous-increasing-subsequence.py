class Solution(object):
    def findLengthOfLCIS(self, nums):
        if not nums:
            return 0
        ans = 0
        count = 0
        for i in range(1,len(nums)):
            if nums[i] > nums[i - 1]:
                count += 1
            else:
                count = 0
            ans = max(ans,count)
        return ans + 1

        