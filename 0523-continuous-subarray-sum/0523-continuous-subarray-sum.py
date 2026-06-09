class Solution(object):
    def checkSubarraySum(self, nums, k):
        freq = {0:-1}
        prefix_sum = 0
        for i in range(len(nums)):
            prefix_sum += nums[i]
            r = prefix_sum % k 
            if r in freq:
                if i - freq[r] >= 2:
                    return True
            else:
                freq[r] = i
        return False