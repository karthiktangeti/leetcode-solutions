class Solution(object):
    def minStartValue(self, nums):
        prefix = 0
        min_prefix = 0
        for num in nums:
            prefix += num
            min_prefix = min(min_prefix,prefix)
        return 1 - min_prefix