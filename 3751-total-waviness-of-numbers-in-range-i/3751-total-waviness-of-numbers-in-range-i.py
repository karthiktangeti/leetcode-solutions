class Solution(object):
    def totalWaviness(self, num1, num2):
        count = 0
        for i in range(num1,num2 + 1):
            s = str(i)
            for j in range(1,len(s) - 1):
                if s[j - 1] < s[j] > s[j + 1]:
                    count += 1
                elif s[j - 1] > s[j] < s[j + 1]:
                    count += 1
        return count


        
        