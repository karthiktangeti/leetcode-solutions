class Solution(object):
    def sumZero(self, n):
        arr = []
        for i in range(1, n // 2 + 1):
            arr.append(i)
            arr.append(-i)
        if n % 2 == 1:
            arr.append(0)
        return arr
            
        