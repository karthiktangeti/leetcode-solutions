class Solution(object):
    def minimumPushes(self, word):
        l = len(word)
        ans = 0
        for i in range(l):
            ans += i //8 + 1
        return ans
        