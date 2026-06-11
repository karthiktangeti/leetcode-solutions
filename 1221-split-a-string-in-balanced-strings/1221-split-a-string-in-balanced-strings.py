class Solution(object):
    def balancedStringSplit(self, s):
        count = 0
        r_count = 0
        l_count = 0
        for i in s:
            if i == "R":
                r_count += 1
            else:
                l_count += 1
            if r_count == l_count:
                count += 1
                r_count = 0
                l_count = 0
        return count
        