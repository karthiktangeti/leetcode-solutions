class Solution(object):
    def leftRightDifference(self, nums):
        right_sum = []*len(nums)
        left_sum = []* len(nums)
        for i in range(len(nums)):
            sum1 = 0
            for j in range(i + 1,len(nums)):
                sum1 += nums[j]
            right_sum.append(sum1)
        for i in range(len(nums)- 1,-1,-1):
            sum1 = 0
            for j in range(i - 1,-1,-1):
                sum1 += nums[j]
            left_sum.append(sum1)
        left_sum = left_sum[::-1]
        for i in range(len(nums)):
            nums[i] = abs(right_sum[i] - left_sum[i])
        return nums
                
        

        