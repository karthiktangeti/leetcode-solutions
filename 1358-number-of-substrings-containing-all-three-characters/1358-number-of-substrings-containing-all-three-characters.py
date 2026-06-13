class Solution(object):
    def numberOfSubstrings(self, s):
        count = {"a":0,"b":0,"c":0}
        n = len(s)
        l = 0
        ans = 0
        for i in range(n):
            count[s[i]] += 1
            while count["a"] > 0 and count["b"] > 0 and count["c"] > 0:
                ans  += n - i
                count[s[l]] -= 1
                l += 1
        return ans      