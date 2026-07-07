class Solution(object):
    def sumAndMultiply(self, n):
        n = str(n)  
        sum1 = 0
        for i in n:
            if i.isdigit() and i != "0":
                sum1 = sum1 * 10 + int(i)
        sum2 = 0
        n = int(sum1)
        while n > 0:
            r = n % 10
            sum2 = sum2+ r
            n //= 10
        return sum1 * sum2

        