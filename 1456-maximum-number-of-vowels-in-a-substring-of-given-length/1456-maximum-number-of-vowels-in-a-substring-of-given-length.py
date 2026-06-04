class Solution(object):
    def maxVowels(self, s, k):
        vowel = ["a","e","i","o","u"]
        count = 0
        for i in range(k):
            if s[i] in vowel:
                count += 1
        ans = count
        for i in range(k,len(s)):
            if s[i - k] in vowel:
                count -= 1
            if s[i] in vowel:
                count += 1
            ans = max(ans,count)
        return ans