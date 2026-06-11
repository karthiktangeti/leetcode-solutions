class Solution(object):
    def countPartitions(self, nums):
        count = 0
        curr = nums[0]
        for i in range(1,len(nums)):
            sum1 = curr - sum(nums[i:])
            if sum1 % 2 == 0:
                count += 1
            curr += nums[i]
        return count
        