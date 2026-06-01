class Solution(object):
    def minimumCost(self, cost):
        sum1 = 0
        cost.sort(reverse = True)
        for i in range(len(cost)):
            if i % 3 != 2:
                sum1 += cost[i]
        return sum1

        