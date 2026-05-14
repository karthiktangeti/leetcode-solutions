class Solution(object):
    def findTheDifference(self, s, t):
        total = 0
        for c in t:
            total += ord(c)
        for c in s:
            total -= ord(c)
        return chr(total)