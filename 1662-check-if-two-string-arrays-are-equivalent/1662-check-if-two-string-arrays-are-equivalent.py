class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        res = ""
        res1 = ""
        for i in word1:
            res += i
        for i in word2:
            res1 += i
        return res == res1