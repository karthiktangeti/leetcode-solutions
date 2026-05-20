class Solution(object):
    def arraySign(self, nums):
        neg = 0
        for n in nums:
            if n == 0:
                return 0
            if n < 0:
                neg += 1
        if neg % 2 == 0:
            return 1
        return -1