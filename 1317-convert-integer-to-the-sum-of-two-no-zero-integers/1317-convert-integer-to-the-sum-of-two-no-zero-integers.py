class Solution(object):
    def noZero(self,x):
        while x:
            if x % 10 == 0:
                return False
            x //= 10
        return True
    def getNoZeroIntegers(self, n):
        for a in range(1,n):
            b  = n - a
            if self.noZero(a) and self.noZero(b):
                return [a,b]
            