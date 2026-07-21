class Solution(object):
    def fairCandySwap(self, aliceSizes, bobSizes):
        sumA = sum(aliceSizes)
        sumB = sum(bobSizes)
        diff = (sumB - sumA) // 2
        bob = set(bobSizes)
        for i in aliceSizes:
            if i + diff in bob:
                return [i,i + diff]
        