class Solution(object):
    def findMin(self, nums):
        mini = float('inf')
        for i in nums:
            if i < mini:
                mini = i
        return mini
        