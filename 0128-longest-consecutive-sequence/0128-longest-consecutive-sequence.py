class Solution(object):
    def longestConsecutive(self, nums):
        if len(nums) == 0:
            return 0
        nums.sort()
        c = 1
        maxi = 1
        for  i in range(1,len(nums)):
            if nums[i] == nums[i - 1]:
                continue
            if nums[i] == nums[i - 1] + 1:
                c += 1 
            else:
                maxi = max(maxi,c)
                c = 1
        r = max(maxi,c)
        return r
