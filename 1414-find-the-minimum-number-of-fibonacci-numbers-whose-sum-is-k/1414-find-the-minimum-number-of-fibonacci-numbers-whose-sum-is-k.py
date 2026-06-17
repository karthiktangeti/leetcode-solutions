class Solution(object):
    def findMinFibonacciNumbers(self, k):
        feb = [1,1]
        while feb[-1] < k:
            feb.append(feb[-1] + feb[-2])
        ans = 0
        for i in range(len(feb) -1,-1 ,-1):
            if feb[i] <= k:
                k -= feb[i]
                ans += 1
            if k == 0:
                return ans
