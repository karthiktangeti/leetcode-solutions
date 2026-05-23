class Solution(object):
    def check(self, nums):
        if nums == sorted(nums):
            return True
        index = -1
        for i in range(1,len(nums)):
            if nums[i] < nums[i - 1]:
                index = i
                break
        nums = nums[index: ] + nums[:index]
        return nums == sorted(nums)