class Solution(object):
    def dominantIndex(self, nums):
        maxi = max(nums)
        for i in range(len(nums)):
            if nums[i] == maxi:
                index= i
        for i in range(len(nums)):
            if nums[i] == maxi:
                continue
            elif nums[i] * 2 > maxi:
                return -1
        return index

            
        