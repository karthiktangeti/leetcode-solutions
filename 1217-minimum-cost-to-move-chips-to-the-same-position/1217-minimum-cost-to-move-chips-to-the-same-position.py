class Solution(object):
    def minCostToMoveChips(self, position):
        o = 0
        e = 0
        for i in position:
            if i % 2:
                o += 1
            else:
                e += 1
        return min(o,e)
        