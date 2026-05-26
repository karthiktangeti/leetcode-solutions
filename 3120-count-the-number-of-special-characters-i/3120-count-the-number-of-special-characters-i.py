class Solution(object):
    def numberOfSpecialChars(self, word):
        lower = set()
        upper = set()
        for i in word:
            if i.islower():
                lower.add(i)
            else:
                upper.add(i.lower())
        return len(lower & upper)