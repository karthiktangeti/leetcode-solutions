class Solution(object):
    def minOperations(self, nums, k):
        nums.sort()
        count = 0
        for i in nums:
            if i >= k:
                break
            else:
                count += 1
        return count
        