class Solution(object):
    def maxProduct(self, n):
        arr =[]
        while n > 0:
            arr.append(n % 10)
            n //= 10
        arr.sort()
        return arr[-1] * arr[-2]
        