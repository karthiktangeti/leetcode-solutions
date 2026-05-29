class Solution(object):
    def minElement(self, nums):
        for i in range(len(nums)):
            sum1 = 0
            while nums[i] > 0:
                sum1 += nums[i] % 10
                nums[i] //= 10
            nums[i] = sum1
        return min(nums)
            
        