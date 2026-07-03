class Solution:
    def countSubstrings(self, s: str) -> int:
        result = []
        def add(l,r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                sub = s[l:r + 1]
                result.append(sub)
                l -= 1
                r += 1
        for i in range(len(s)):
            add(i,i)
            add(i,i+1)
        return len(result)