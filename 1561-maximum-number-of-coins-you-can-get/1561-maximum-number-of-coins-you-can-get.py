class Solution(object):
    def maxCoins(self, piles):
        piles.sort()
        n = len(piles) // 3
        sum1 = 0
        for i in range(n,len(piles),2):
            sum1 += piles[i]
        return sum1

        