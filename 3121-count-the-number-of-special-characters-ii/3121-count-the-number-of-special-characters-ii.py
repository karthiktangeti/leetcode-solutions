class Solution(object):
    def numberOfSpecialChars(self, word):
        lastlower = {}
        firstupper = {}
        for i,ch in enumerate(word):
            if ch.islower():
                lastlower[ch] = i
            else:
                firstupper.setdefault(ch.lower(),i)
        count = 0
        for ch in lastlower:
            if ch in firstupper and lastlower[ch] < firstupper[ch]:
                count += 1
        return count
