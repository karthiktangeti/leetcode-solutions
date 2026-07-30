class Solution(object):
    def minCost(self, startPos, homePos, rowCosts, colCosts):
        r1,c1 = startPos
        r2,c2 = homePos
        res = 0
        if r2 >= r1:
            for i in range(r1 + 1,r2 + 1):
                res += rowCosts[i]
        else:
            for i in range(r2,r1):
                res += rowCosts[i]
        if c2 >= c1:
            for i in range(c1 + 1,c2 + 1):
                res += colCosts[i]
        else:
            for i in range(c2,c1):
                res += colCosts[i]
        return res


        