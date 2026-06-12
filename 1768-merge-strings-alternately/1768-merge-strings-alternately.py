class Solution(object):
    def mergeAlternately(self, word1, word2):
        r = 0
        l = 0
        re = ""
        while l < len(word1) or r < len(word2):
            if l < len(word1):
                re += word1[l]
                l += 1
            if r < len(word2):
                re += word2[r]
                r += 1
        return re

        