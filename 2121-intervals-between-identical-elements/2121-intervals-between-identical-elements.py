from collections import defaultdict
from typing import List
class Solution:
    def getDistances(self, arr: List[int]) -> List[int]:
        n = len(arr)
        ans = [0] * n
        left = defaultdict(lambda:[0,0])
        for i ,v in enumerate(arr):
            count,total = left[v]
            ans[i] += i * count - total
            left[v][0] += 1
            left[v][1] += i
        right = defaultdict(lambda:[0,0])
        for i in range(n - 1,-1,-1):
            v = arr[i]
            count,total = right[v]
            ans[i] += total - i * count
            right[v][0] += 1
            right[v][1] += i
        return ans
        