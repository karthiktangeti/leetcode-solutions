class Solution(object):
    def findRepeatedDnaSequences(self, s):
        seen = {}
        arr = []
        for i in range(len(s) - 9):
            sub = s[i:i+10]
            seen[sub] = seen.get(sub,0) + 1
        for key,val in seen.items():
            if val > 1:
                arr.append(key)
        return arr
