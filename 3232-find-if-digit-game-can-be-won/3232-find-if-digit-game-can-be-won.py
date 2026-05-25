class Solution(object):
    def canAliceWin(self, nums):
        a_sum = 0
        b_sum = 0
        for i in nums:
            if len(str(i)) == 1:
                a_sum += i
            else:
                b_sum += i
        if a_sum > b_sum or b_sum > a_sum:
            return True
        return False