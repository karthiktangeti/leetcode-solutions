class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        start = 0
        total = 0
        tank = 0
        for i in range(len(gas)):
            total += gas[i] - cost[i]
            tank += gas[i] - cost[i]
            if tank < 0:
                start = i + 1
                tank = 0
        return start if total >= 0 else -1
        