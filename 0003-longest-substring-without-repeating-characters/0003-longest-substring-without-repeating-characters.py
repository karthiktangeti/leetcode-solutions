class Solution(object):
    def lengthOfLongestSubstring(self, s):
        l,maxi = 0,0
        n = len(s)
        temp = []
        for i in range(n):
            temp.append(s[i])

            while len(temp) != len(set(temp)):
                temp.pop(0)
                l += 1
            maxi = max(maxi,i - l + 1)
        return maxi
        