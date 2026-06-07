class Solution(object):
    def countGoodSubstrings(self, s):
        n = len(s)
        ans = 0
        l= 0
        temp = []
        for i in range(n):
            temp.append(s[i])
            if i - l == 3:
                temp.pop(0)
                l += 1
            if len(temp) == 3 and len(set(temp)) == 3:
                ans += 1

        return ans
        