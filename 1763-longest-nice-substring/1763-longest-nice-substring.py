class Solution(object):
    def longestNiceSubstring(self, s):
        def func(sub):
            st = set(sub)
            for ch in sub:
                if ch.lower() not in sub or ch.upper() not in sub:
                    return False
            return True
        ans = ""
        for i in range(len(s)):
            for j in range(i + 1,len(s) + 1):
                sub = s[i:j]
                if func(sub) and len(sub) > len(ans):
                    ans = sub
        return ans
        