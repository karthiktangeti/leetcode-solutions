class Solution:
    def addMinimum(self, word: str) -> int:
        group = 1
        for i in range(1,len(word)):
            if word[i] <= word[i - 1]:
                group += 1
        return group * 3 - len(word)
        
        