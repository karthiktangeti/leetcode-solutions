class Solution(object):
    def separateDigits(self, nums):
        result = []
        for i in nums:
            digits = str(i)
            for d in digits:
                result.append(int(d))
        return result
        